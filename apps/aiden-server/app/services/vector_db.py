from typing import List, Dict, Any, Optional
import time
from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
from sentence_transformers import SentenceTransformer
from app.core.config import settings

class VectorDBService:
    def __init__(self):
        self.host = settings.MILVUS_HOST
        self.port = settings.MILVUS_PORT
        self.collection_name = "successful_emails"
        self.dim = 384  # Dimension for all-MiniLM-L6-v2

        # Load embedding model (lazy load could be better for startup time, but good for now)
        # Using a small, efficient model for free CPU inference
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def connect(self):
        try:
            connections.connect("default", host=self.host, port=self.port)
            print(f"Connected to Milvus at {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to Milvus: {e}")

    def create_collection(self):
        """
        Create the collection if it doesn't exist.
        """
        self.connect()

        if utility.has_collection(self.collection_name):
            print(f"Collection {self.collection_name} already exists.")
            return

        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=self.dim),
            FieldSchema(name="subject", dtype=DataType.VARCHAR, max_length=500),
            FieldSchema(name="body", dtype=DataType.VARCHAR, max_length=5000),
            FieldSchema(name="industry", dtype=DataType.VARCHAR, max_length=100),
        ]

        schema = CollectionSchema(fields, "Collection for successful email drafts")
        collection = Collection(self.collection_name, schema)

        # Create index for faster search
        index_params = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128},
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        print(f"Collection {self.collection_name} created.")

    def add_email(self, subject: str, body: str, industry: str = "General"):
        """
        Vectorize and save an email to Milvus.
        """
        self.connect()

        # Create embedding from body (could combine subject + body)
        text_to_embed = f"{subject}\n\n{body}"
        embedding = self.model.encode(text_to_embed).tolist()

        collection = Collection(self.collection_name)

        entities = [
            [embedding],  # embedding
            [subject],    # subject
            [body],       # body
            [industry],   # industry
        ]

        collection.insert(entities)
        print(f"Inserted email: {subject}")

    def search_similar_emails(self, query_text: str, limit: int = 3) -> List[Dict[str, Any]]:
        """
        Find similar emails to the query text (RAG context).
        """
        self.connect()
        collection = Collection(self.collection_name)
        collection.load()

        query_embedding = self.model.encode(query_text).tolist()

        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }

        results = collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param=search_params,
            limit=limit,
            output_fields=["subject", "body", "industry"]
        )

        found_emails = []
        for hits in results:
            for hit in hits:
                found_emails.append({
                    "id": hit.id,
                    "score": hit.distance,
                    "subject": hit.entity.get("subject"),
                    "body": hit.entity.get("body"),
                    "industry": hit.entity.get("industry"),
                })

        return found_emails

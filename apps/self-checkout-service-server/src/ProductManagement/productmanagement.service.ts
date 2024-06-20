import { Injectable } from "@nestjs/common";
import { ProductDto } from "../productManagement/ProductDto";

@Injectable()
export class ProductManagementService {
  constructor() {}
  async AddProduct(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async CreateProduct(args: ProductDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async DeleteProduct(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async EditProduct(args: ProductDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async UpdateProduct(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
}

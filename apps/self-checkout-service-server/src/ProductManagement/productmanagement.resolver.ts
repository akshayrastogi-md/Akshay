import * as graphql from "@nestjs/graphql";
import { ProductDto } from "../productManagement/ProductDto";
import { ProductManagementService } from "./productmanagement.service";

export class ProductManagementResolver {
  constructor(protected readonly service: ProductManagementService) {}

  @graphql.Query(() => String)
  async AddProduct(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.AddProduct(args);
  }

  @graphql.Mutation(() => String)
  async CreateProduct(
    @graphql.Args()
    args: ProductDto
  ): Promise<string> {
    return this.service.CreateProduct(args);
  }

  @graphql.Mutation(() => String)
  async DeleteProduct(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.DeleteProduct(args);
  }

  @graphql.Mutation(() => String)
  async EditProduct(
    @graphql.Args()
    args: ProductDto
  ): Promise<string> {
    return this.service.EditProduct(args);
  }

  @graphql.Query(() => String)
  async UpdateProduct(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.UpdateProduct(args);
  }
}

import * as graphql from "@nestjs/graphql";
import { CartDto } from "../cartManagement/CartDto";
import { CartManagementService } from "./cartmanagement.service";

export class CartManagementResolver {
  constructor(protected readonly service: CartManagementService) {}

  @graphql.Query(() => String)
  async AddToCart(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.AddToCart(args);
  }

  @graphql.Mutation(() => String)
  async AddToCart(
    @graphql.Args()
    args: CartDto
  ): Promise<string> {
    return this.service.AddToCart(args);
  }

  @graphql.Mutation(() => String)
  async RemoveFromCart(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.RemoveFromCart(args);
  }

  @graphql.Query(() => String)
  async ViewCart(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.ViewCart(args);
  }
}

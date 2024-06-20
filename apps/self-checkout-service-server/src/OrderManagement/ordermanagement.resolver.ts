import * as graphql from "@nestjs/graphql";
import { OrderDto } from "../orderManagement/OrderDto";
import { OrderManagementService } from "./ordermanagement.service";

export class OrderManagementResolver {
  constructor(protected readonly service: OrderManagementService) {}

  @graphql.Mutation(() => String)
  async CreateNewOrder(
    @graphql.Args()
    args: OrderDto
  ): Promise<string> {
    return this.service.CreateNewOrder(args);
  }

  @graphql.Query(() => String)
  async CreateOrder(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.CreateOrder(args);
  }

  @graphql.Mutation(() => String)
  async EditOrder(
    @graphql.Args()
    args: OrderDto
  ): Promise<string> {
    return this.service.EditOrder(args);
  }

  @graphql.Query(() => String)
  async ManageOrder(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.ManageOrder(args);
  }

  @graphql.Query(() => String)
  async ViewOrders(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.ViewOrders(args);
  }
}

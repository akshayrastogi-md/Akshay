import { Injectable } from "@nestjs/common";
import { OrderDto } from "../orderManagement/OrderDto";

@Injectable()
export class OrderManagementService {
  constructor() {}
  async CreateNewOrder(args: OrderDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async CreateOrder(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async EditOrder(args: OrderDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async ManageOrder(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async ViewOrders(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
}

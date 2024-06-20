import { Injectable } from "@nestjs/common";
import { CartDto } from "../cartManagement/CartDto";

@Injectable()
export class CartManagementService {
  constructor() {}
  async AddToCart(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async AddToCart(args: CartDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async RemoveFromCart(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async ViewCart(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
}

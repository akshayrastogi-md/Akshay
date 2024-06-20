import { Cart } from "../cart/Cart";
import { Order } from "../order/Order";
import { JsonValue } from "type-fest";

export type User = {
  accessToken: string | null;
  carts?: Array<Cart>;
  createdAt: Date;
  email: string | null;
  firstName: string | null;
  id: string;
  lastName: string | null;
  mobileNumber: string | null;
  orders?: Array<Order>;
  role?: "Option1" | null;
  roles: JsonValue;
  updatedAt: Date;
  username: string;
};

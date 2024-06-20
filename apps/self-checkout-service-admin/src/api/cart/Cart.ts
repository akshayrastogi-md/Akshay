import { JsonValue } from "type-fest";
import { Order } from "../order/Order";
import { User } from "../user/User";

export type Cart = {
  createdAt: Date;
  id: string;
  items: JsonValue;
  orders?: Array<Order>;
  updatedAt: Date;
  user?: User | null;
};

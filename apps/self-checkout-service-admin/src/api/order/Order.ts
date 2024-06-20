import { Cart } from "../cart/Cart";
import { Payment } from "../payment/Payment";
import { User } from "../user/User";

export type Order = {
  cart?: Cart | null;
  createdAt: Date;
  id: string;
  paymentMethod?: "Option1" | null;
  payments?: Array<Payment>;
  paymentStatus?: "Option1" | null;
  totalAmount: number | null;
  updatedAt: Date;
  user?: User | null;
};

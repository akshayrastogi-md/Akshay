import { OrderWhereUniqueInput } from "../order/OrderWhereUniqueInput";

export type PaymentUpdateInput = {
  amount?: number | null;
  order?: OrderWhereUniqueInput | null;
  paymentMethod?: "Option1" | null;
  status?: "Option1" | null;
};

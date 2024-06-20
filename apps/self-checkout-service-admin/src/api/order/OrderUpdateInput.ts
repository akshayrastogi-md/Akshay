import { CartWhereUniqueInput } from "../cart/CartWhereUniqueInput";
import { PaymentUpdateManyWithoutOrdersInput } from "./PaymentUpdateManyWithoutOrdersInput";
import { UserWhereUniqueInput } from "../user/UserWhereUniqueInput";

export type OrderUpdateInput = {
  cart?: CartWhereUniqueInput | null;
  paymentMethod?: "Option1" | null;
  payments?: PaymentUpdateManyWithoutOrdersInput;
  paymentStatus?: "Option1" | null;
  totalAmount?: number | null;
  user?: UserWhereUniqueInput | null;
};

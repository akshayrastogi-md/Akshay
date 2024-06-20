import { CartWhereUniqueInput } from "../cart/CartWhereUniqueInput";
import { PaymentCreateNestedManyWithoutOrdersInput } from "./PaymentCreateNestedManyWithoutOrdersInput";
import { UserWhereUniqueInput } from "../user/UserWhereUniqueInput";

export type OrderCreateInput = {
  cart?: CartWhereUniqueInput | null;
  paymentMethod?: "Option1" | null;
  payments?: PaymentCreateNestedManyWithoutOrdersInput;
  paymentStatus?: "Option1" | null;
  totalAmount?: number | null;
  user?: UserWhereUniqueInput | null;
};

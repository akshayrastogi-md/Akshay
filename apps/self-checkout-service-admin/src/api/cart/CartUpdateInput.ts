import { InputJsonValue } from "../../types";
import { OrderUpdateManyWithoutCartsInput } from "./OrderUpdateManyWithoutCartsInput";
import { UserWhereUniqueInput } from "../user/UserWhereUniqueInput";

export type CartUpdateInput = {
  items?: InputJsonValue;
  orders?: OrderUpdateManyWithoutCartsInput;
  user?: UserWhereUniqueInput | null;
};

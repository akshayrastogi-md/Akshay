import { InputJsonValue } from "../../types";
import { OrderCreateNestedManyWithoutCartsInput } from "./OrderCreateNestedManyWithoutCartsInput";
import { UserWhereUniqueInput } from "../user/UserWhereUniqueInput";

export type CartCreateInput = {
  items?: InputJsonValue;
  orders?: OrderCreateNestedManyWithoutCartsInput;
  user?: UserWhereUniqueInput | null;
};

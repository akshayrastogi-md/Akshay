import { CartUpdateManyWithoutUsersInput } from "./CartUpdateManyWithoutUsersInput";
import { OrderUpdateManyWithoutUsersInput } from "./OrderUpdateManyWithoutUsersInput";
import { InputJsonValue } from "../../types";

export type UserUpdateInput = {
  accessToken?: string | null;
  carts?: CartUpdateManyWithoutUsersInput;
  email?: string | null;
  firstName?: string | null;
  lastName?: string | null;
  mobileNumber?: string | null;
  orders?: OrderUpdateManyWithoutUsersInput;
  password?: string;
  role?: "Option1" | null;
  roles?: InputJsonValue;
  username?: string;
};

import { CartCreateNestedManyWithoutUsersInput } from "./CartCreateNestedManyWithoutUsersInput";
import { OrderCreateNestedManyWithoutUsersInput } from "./OrderCreateNestedManyWithoutUsersInput";
import { InputJsonValue } from "../../types";

export type UserCreateInput = {
  accessToken?: string | null;
  carts?: CartCreateNestedManyWithoutUsersInput;
  email?: string | null;
  firstName?: string | null;
  lastName?: string | null;
  mobileNumber?: string | null;
  orders?: OrderCreateNestedManyWithoutUsersInput;
  password: string;
  role?: "Option1" | null;
  roles: InputJsonValue;
  username: string;
};

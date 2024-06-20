import { StringNullableFilter } from "../../util/StringNullableFilter";
import { CartListRelationFilter } from "../cart/CartListRelationFilter";
import { StringFilter } from "../../util/StringFilter";
import { OrderListRelationFilter } from "../order/OrderListRelationFilter";

export type UserWhereInput = {
  accessToken?: StringNullableFilter;
  carts?: CartListRelationFilter;
  email?: StringNullableFilter;
  firstName?: StringNullableFilter;
  id?: StringFilter;
  lastName?: StringNullableFilter;
  mobileNumber?: StringNullableFilter;
  orders?: OrderListRelationFilter;
  role?: "Option1";
  username?: StringFilter;
};

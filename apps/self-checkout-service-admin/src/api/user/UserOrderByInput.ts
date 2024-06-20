import { SortOrder } from "../../util/SortOrder";

export type UserOrderByInput = {
  accessToken?: SortOrder;
  createdAt?: SortOrder;
  email?: SortOrder;
  firstName?: SortOrder;
  id?: SortOrder;
  lastName?: SortOrder;
  mobileNumber?: SortOrder;
  password?: SortOrder;
  role?: SortOrder;
  roles?: SortOrder;
  updatedAt?: SortOrder;
  username?: SortOrder;
};

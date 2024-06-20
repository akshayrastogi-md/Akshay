import { SortOrder } from "../../util/SortOrder";

export type CartOrderByInput = {
  createdAt?: SortOrder;
  id?: SortOrder;
  items?: SortOrder;
  updatedAt?: SortOrder;
  userId?: SortOrder;
};

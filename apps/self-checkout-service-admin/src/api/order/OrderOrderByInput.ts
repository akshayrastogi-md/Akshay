import { SortOrder } from "../../util/SortOrder";

export type OrderOrderByInput = {
  cartId?: SortOrder;
  createdAt?: SortOrder;
  id?: SortOrder;
  paymentMethod?: SortOrder;
  paymentStatus?: SortOrder;
  totalAmount?: SortOrder;
  updatedAt?: SortOrder;
  userId?: SortOrder;
};

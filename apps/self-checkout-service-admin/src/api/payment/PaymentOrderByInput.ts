import { SortOrder } from "../../util/SortOrder";

export type PaymentOrderByInput = {
  amount?: SortOrder;
  createdAt?: SortOrder;
  id?: SortOrder;
  orderId?: SortOrder;
  paymentMethod?: SortOrder;
  status?: SortOrder;
  updatedAt?: SortOrder;
};

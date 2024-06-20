import { Cart as TCart } from "../api/cart/Cart";

export const CART_TITLE_FIELD = "id";

export const CartTitle = (record: TCart): string => {
  return record.id?.toString() || String(record.id);
};

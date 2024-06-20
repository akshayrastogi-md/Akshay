/*
------------------------------------------------------------------------------ 
This code was generated by Amplication. 
 
Changes to this file will be lost if the code is regenerated. 

There are other ways to to customize your code, see this doc to learn more
https://docs.amplication.com/how-to/custom-code

------------------------------------------------------------------------------
  */
import { PrismaService } from "../../prisma/prisma.service";
import {
  Prisma,
  Cart as PrismaCart,
  Order as PrismaOrder,
  User as PrismaUser,
} from "@prisma/client";

export class CartServiceBase {
  constructor(protected readonly prisma: PrismaService) {}

  async count(args: Omit<Prisma.CartCountArgs, "select">): Promise<number> {
    return this.prisma.cart.count(args);
  }

  async carts(args: Prisma.CartFindManyArgs): Promise<PrismaCart[]> {
    return this.prisma.cart.findMany(args);
  }
  async cart(args: Prisma.CartFindUniqueArgs): Promise<PrismaCart | null> {
    return this.prisma.cart.findUnique(args);
  }
  async createCart(args: Prisma.CartCreateArgs): Promise<PrismaCart> {
    return this.prisma.cart.create(args);
  }
  async updateCart(args: Prisma.CartUpdateArgs): Promise<PrismaCart> {
    return this.prisma.cart.update(args);
  }
  async deleteCart(args: Prisma.CartDeleteArgs): Promise<PrismaCart> {
    return this.prisma.cart.delete(args);
  }

  async findOrders(
    parentId: string,
    args: Prisma.OrderFindManyArgs
  ): Promise<PrismaOrder[]> {
    return this.prisma.cart
      .findUniqueOrThrow({
        where: { id: parentId },
      })
      .orders(args);
  }

  async getUser(parentId: string): Promise<PrismaUser | null> {
    return this.prisma.cart
      .findUnique({
        where: { id: parentId },
      })
      .user();
  }
}

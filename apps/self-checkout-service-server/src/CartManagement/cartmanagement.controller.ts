import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { CartManagementService } from "./cartmanagement.service";

@swagger.ApiTags("cartManagements")
@common.Controller("cartManagements")
export class CartManagementController {
  constructor(protected readonly service: CartManagementService) {}

  @common.Get("/:id/add-to-cart")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async AddToCart(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.AddToCart(body);
      }

  @common.Post("/add-to-cart")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async AddToCart(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.AddToCart(body);
      }

  @common.Delete("/remove-from-cart/:id")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async RemoveFromCart(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.RemoveFromCart(body);
      }

  @common.Get("/view-cart")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async ViewCart(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.ViewCart(body);
      }
}

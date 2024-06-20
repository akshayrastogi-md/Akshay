import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { OrderManagementService } from "./ordermanagement.service";

@swagger.ApiTags("orderManagements")
@common.Controller("orderManagements")
export class OrderManagementController {
  constructor(protected readonly service: OrderManagementService) {}

  @common.Post("/create-new-order")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CreateNewOrder(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.CreateNewOrder(body);
      }

  @common.Get("/:id/create-order")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CreateOrder(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.CreateOrder(body);
      }

  @common.Put("/edit-order/:id")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async EditOrder(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.EditOrder(body);
      }

  @common.Get("/:id/manage-order")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async ManageOrder(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.ManageOrder(body);
      }

  @common.Get("/view-orders")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async ViewOrders(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.ViewOrders(body);
      }
}

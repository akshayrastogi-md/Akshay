import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { ProductManagementService } from "./productmanagement.service";

@swagger.ApiTags("productManagements")
@common.Controller("productManagements")
export class ProductManagementController {
  constructor(protected readonly service: ProductManagementService) {}

  @common.Get("/:id/add-product")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async AddProduct(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.AddProduct(body);
      }

  @common.Post("/create-product")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CreateProduct(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.CreateProduct(body);
      }

  @common.Delete("/delete-product/:id")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async DeleteProduct(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.DeleteProduct(body);
      }

  @common.Put("/edit-product/:id")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async EditProduct(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.EditProduct(body);
      }

  @common.Get("/:id/update-product")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async UpdateProduct(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.UpdateProduct(body);
      }
}

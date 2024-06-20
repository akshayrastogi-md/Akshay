import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { PaymentProcessingService } from "./paymentprocessing.service";
import { PaymentDto } from "../paymentProcessing/PaymentDto";

@swagger.ApiTags("paymentProcessings")
@common.Controller("paymentProcessings")
export class PaymentProcessingController {
  constructor(protected readonly service: PaymentProcessingService) {}

  @common.Get("/:id/complete-payment")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CompletePayment(
    @common.Body()
    body: PaymentDto
  ): Promise<string> {
        return this.service.CompletePayment(body);
      }

  @common.Put("/finalize-payment/:id")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async FinalizePayment(
    @common.Body()
    body: PaymentDto
  ): Promise<string> {
        return this.service.FinalizePayment(body);
      }

  @common.Get("/:id/initiate-payment")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async InitiatePayment(
    @common.Body()
    body: PaymentDto
  ): Promise<string> {
        return this.service.InitiatePayment(body);
      }

  @common.Post("/start-payment")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async StartPayment(
    @common.Body()
    body: PaymentDto
  ): Promise<string> {
        return this.service.StartPayment(body);
      }
}

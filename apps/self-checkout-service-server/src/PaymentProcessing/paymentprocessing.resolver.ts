import * as graphql from "@nestjs/graphql";
import { PaymentDto } from "../paymentProcessing/PaymentDto";
import { PaymentProcessingService } from "./paymentprocessing.service";

export class PaymentProcessingResolver {
  constructor(protected readonly service: PaymentProcessingService) {}

  @graphql.Query(() => String)
  async CompletePayment(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.CompletePayment(args);
  }

  @graphql.Mutation(() => String)
  async FinalizePayment(
    @graphql.Args()
    args: PaymentDto
  ): Promise<string> {
    return this.service.FinalizePayment(args);
  }

  @graphql.Query(() => String)
  async InitiatePayment(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.InitiatePayment(args);
  }

  @graphql.Mutation(() => String)
  async StartPayment(
    @graphql.Args()
    args: PaymentDto
  ): Promise<string> {
    return this.service.StartPayment(args);
  }
}

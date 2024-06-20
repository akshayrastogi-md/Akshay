import { Injectable } from "@nestjs/common";
import { PaymentDto } from "../paymentProcessing/PaymentDto";

@Injectable()
export class PaymentProcessingService {
  constructor() {}
  async CompletePayment(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async FinalizePayment(args: PaymentDto): Promise<string> {
    throw new Error("Not implemented");
  }
  async InitiatePayment(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async StartPayment(args: PaymentDto): Promise<string> {
    throw new Error("Not implemented");
  }
}

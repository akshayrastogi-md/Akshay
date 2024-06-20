import { Module } from "@nestjs/common";
import { PaymentProcessingService } from "./paymentprocessing.service";
import { PaymentProcessingController } from "./paymentprocessing.controller";
import { PaymentProcessingResolver } from "./paymentprocessing.resolver";

@Module({
  controllers: [PaymentProcessingController],
  providers: [PaymentProcessingService, PaymentProcessingResolver],
  exports: [PaymentProcessingService],
})
export class PaymentProcessingModule {}

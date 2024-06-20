import { Module } from "@nestjs/common";
import { OrderManagementService } from "./ordermanagement.service";
import { OrderManagementController } from "./ordermanagement.controller";
import { OrderManagementResolver } from "./ordermanagement.resolver";

@Module({
  controllers: [OrderManagementController],
  providers: [OrderManagementService, OrderManagementResolver],
  exports: [OrderManagementService],
})
export class OrderManagementModule {}

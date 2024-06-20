import { Module } from "@nestjs/common";
import { CartManagementService } from "./cartmanagement.service";
import { CartManagementController } from "./cartmanagement.controller";
import { CartManagementResolver } from "./cartmanagement.resolver";

@Module({
  controllers: [CartManagementController],
  providers: [CartManagementService, CartManagementResolver],
  exports: [CartManagementService],
})
export class CartManagementModule {}

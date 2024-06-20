import { Module } from "@nestjs/common";
import { ProductManagementService } from "./productmanagement.service";
import { ProductManagementController } from "./productmanagement.controller";
import { ProductManagementResolver } from "./productmanagement.resolver";

@Module({
  controllers: [ProductManagementController],
  providers: [ProductManagementService, ProductManagementResolver],
  exports: [ProductManagementService],
})
export class ProductManagementModule {}

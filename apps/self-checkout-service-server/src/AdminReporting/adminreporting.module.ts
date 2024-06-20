import { Module } from "@nestjs/common";
import { AdminReportingService } from "./adminreporting.service";
import { AdminReportingController } from "./adminreporting.controller";
import { AdminReportingResolver } from "./adminreporting.resolver";

@Module({
  controllers: [AdminReportingController],
  providers: [AdminReportingService, AdminReportingResolver],
  exports: [AdminReportingService],
})
export class AdminReportingModule {}

import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { AdminReportingService } from "./adminreporting.service";

@swagger.ApiTags("adminReportings")
@common.Controller("adminReportings")
export class AdminReportingController {
  constructor(protected readonly service: AdminReportingService) {}

  @common.Get("/view-sales-report")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async ViewSalesReport(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.ViewSalesReport(body);
      }

  @common.Get("/view-user-report")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async ViewUserReport(
    @common.Body()
    body: string
  ): Promise<string> {
        return this.service.ViewUserReport(body);
      }
}

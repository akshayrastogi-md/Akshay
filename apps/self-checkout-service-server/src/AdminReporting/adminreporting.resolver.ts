import * as graphql from "@nestjs/graphql";
import { AdminReportingService } from "./adminreporting.service";

export class AdminReportingResolver {
  constructor(protected readonly service: AdminReportingService) {}

  @graphql.Query(() => String)
  async ViewSalesReport(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.ViewSalesReport(args);
  }

  @graphql.Query(() => String)
  async ViewUserReport(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.ViewUserReport(args);
  }
}

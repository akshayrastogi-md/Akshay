import { Injectable } from "@nestjs/common";

@Injectable()
export class AdminReportingService {
  constructor() {}
  async ViewSalesReport(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async ViewUserReport(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
}

import * as graphql from "@nestjs/graphql";
import { AuthService } from "./auth.service";

export class AuthResolver {
  constructor(protected readonly service: AuthService) {}

  @graphql.Mutation(() => String)
  async UserLogin(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.UserLogin(args);
  }

  @graphql.Mutation(() => String)
  async UserRegistration(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.UserRegistration(args);
  }
}

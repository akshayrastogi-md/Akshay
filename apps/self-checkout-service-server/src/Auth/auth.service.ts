import { Injectable } from "@nestjs/common";

@Injectable()
export class AuthService {
  constructor() {}
  async UserLogin(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async UserRegistration(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
}

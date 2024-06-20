import { Module } from "@nestjs/common";
import { PaymentModule } from "./payment/payment.module";
import { CartModule } from "./cart/cart.module";
import { ProductModule } from "./product/product.module";
import { OrderModule } from "./order/order.module";
import { UserModule } from "./user/user.module";
import { AdminReportingModule } from "./AdminReporting/adminreporting.module";
import { AuthModule } from "./Auth/auth.module";
import { CartManagementModule } from "./CartManagement/cartmanagement.module";
import { OrderManagementModule } from "./OrderManagement/ordermanagement.module";
import { PaymentProcessingModule } from "./PaymentProcessing/paymentprocessing.module";
import { ProductManagementModule } from "./ProductManagement/productmanagement.module";
import { HealthModule } from "./health/health.module";
import { PrismaModule } from "./prisma/prisma.module";
import { SecretsManagerModule } from "./providers/secrets/secretsManager.module";
import { ServeStaticModule } from "@nestjs/serve-static";
import { ServeStaticOptionsService } from "./serveStaticOptions.service";
import { ConfigModule, ConfigService } from "@nestjs/config";
import { GraphQLModule } from "@nestjs/graphql";
import { ApolloDriver, ApolloDriverConfig } from "@nestjs/apollo";

import { ACLModule } from "./auth/acl.module";
import { AuthModule } from "./auth/auth.module";

@Module({
  controllers: [],
  imports: [
    ACLModule,
    AuthModule,
    PaymentModule,
    CartModule,
    ProductModule,
    OrderModule,
    UserModule,
    AdminReportingModule,
    AuthModule,
    CartManagementModule,
    OrderManagementModule,
    PaymentProcessingModule,
    ProductManagementModule,
    HealthModule,
    PrismaModule,
    SecretsManagerModule,
    ConfigModule.forRoot({ isGlobal: true }),
    ServeStaticModule.forRootAsync({
      useClass: ServeStaticOptionsService,
    }),
    GraphQLModule.forRootAsync<ApolloDriverConfig>({
      driver: ApolloDriver,
      useFactory: (configService: ConfigService) => {
        const playground = configService.get("GRAPHQL_PLAYGROUND");
        const introspection = configService.get("GRAPHQL_INTROSPECTION");
        return {
          autoSchemaFile: "schema.graphql",
          sortSchema: true,
          playground,
          introspection: playground || introspection,
        };
      },
      inject: [ConfigService],
      imports: [ConfigModule],
    }),
  ],
  providers: [],
})
export class AppModule {}

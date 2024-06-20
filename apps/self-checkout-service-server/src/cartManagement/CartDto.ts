import { ArgsType, Field } from "@nestjs/graphql";
import { GraphQLJSON } from "graphql-type-json";
import { InputJsonValue } from "../types";

@ArgsType()
class CartDto {
    @Field(() => GraphQLJSON)
    items!: InputJsonValue;
}

export { CartDto as CartDto };
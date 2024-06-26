import * as React from "react";
import {
  Create,
  SimpleForm,
  CreateProps,
  TextInput,
  NumberInput,
} from "react-admin";

export const ProductCreate = (props: CreateProps): React.ReactElement => {
  return (
    <Create {...props}>
      <SimpleForm>
        <TextInput label="barcode" source="barcode" />
        <NumberInput label="discount" source="discount" />
        <TextInput label="name" source="name" />
        <NumberInput label="price" source="price" />
      </SimpleForm>
    </Create>
  );
};

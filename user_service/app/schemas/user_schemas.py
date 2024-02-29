import marshmallow as ma


class CreateUserSchema(ma.Schema):
    first_name = ma.fields.String()
    last_name = ma.fields.String()
    email = ma.fields.Email()
    password = ma.fields.String()


class UserListSchema(ma.Schema):
    first_name = ma.fields.String()
    last_name = ma.fields.String()
    email = ma.fields.Email()


class UserLoginSchema(ma.Schema):
    email = ma.fields.Email()
    password = ma.fields.String()

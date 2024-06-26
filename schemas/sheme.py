import flask_marshmallow as ma


class SchemaBase(ma.Schema):
    @classmethod
    def schema_many(cls, arg):
        if len(arg) > 1:
            return cls(many=True).dump(arg)
        else:
            return cls(many=False).dump(arg[0])


class TodoTaskSchema(SchemaBase, ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'time', 'list_id')


class TodoListSchema(SchemaBase, ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'user_id')


class UserSchema(SchemaBase, ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')


todo_schema = TodoTaskSchema(many=False)
todos_schema = TodoTaskSchema(many=True)

todo_lists_schema = TodoListSchema(many=True)

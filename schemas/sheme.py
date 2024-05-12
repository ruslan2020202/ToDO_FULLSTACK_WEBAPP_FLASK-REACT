import flask_marshmallow as ma


class TodoListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'time')


todo_schema = TodoListSchema(many=False)
todos_schema = TodoListSchema(many=True)

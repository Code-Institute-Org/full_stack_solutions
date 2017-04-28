# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.serializers import TodoSerializer
from todo.models import Todo


class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """

    def get(self, request):
        """
        Retrieve a complete list of `todo` items from the Todo
        model, serialize them to JSON and return the serialized 
        todo items
        """
        todo_items = Todo.objects.all()
        # Serialize the data retrieved from the DB and serialize
        # them using the `TodoSerializer`
        serializer = TodoSerializer(todo_items, many=True)
        # Store the serialized data `serialized_data`
        serialized_data = serializer.data
        return Response(serialized_data)
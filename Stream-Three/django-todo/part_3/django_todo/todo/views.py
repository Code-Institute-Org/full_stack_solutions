# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo


class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """

    def get(self, request, pk=None):
        """
        Handle the GET request for the `/todo/` endpoint.

        Checks to see if a primary key has been provided by the URL.
        If not, a full list of `todo` will be retrieved. If a primary key 
        has been provided then only that instance will be retrieved

        Returns the serialized `todo` object(s).
        """
        if pk is None:
            todo_items = Todo.objects.all()
            # Serialize the data retrieved from the DB and serialize
            # them using the `TodoSerializer`
            serializer = TodoSerializer(todo_items, many=True)
            # Store the serialized data `serialized_data`
            serialized_data = serializer.data
            return Response(serialized_data)
        else:
            # Get the object containing the pk provided by the URL
            todo = Todo.objects.get(id=pk)
            # Serialize the `todo` item
            serializer = TodoSerializer(todo)
            # Store it in the serialized_data variable and return it
            serialized_data = serializer.data
            return Response(serialized_data)

    def post(self, request):
        """
        Handle the POST request for the `/todo/` endpoint.

        This view will take the `data` property from the `request` object,
        deserialize it into a `Todo` object and store in the DB

        Returns a 201 (successfully created) if the item is successfully
        created, otherwise returns a 400 (bad request)
        """
        serializer = TodoSerializer(data=request.data)

        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request respose will be returned containing the error.
        # Else, save the data and return the data and a successfully
        # created status
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        """
        Handle PUT request for the `/todo/` endpoint.

        Retrieves a `todo` instance based on the primary key contained
        in the URL. Then takes the `data` property from the `request` object
        to update the relevant `todo` instance.

        Returns the updated object if the update was successful, otherwise
        400 (bad request) is returned
        """
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)

        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request respose will be returned containing the error.
        # Else, save and return the data.
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        """
        Handle DELETE request for the `/todo/` endpoint.

        Retrieves a `todo` instance based on the primary key contained
        in the URL and then deletes the relevant instance.

        Returns a 204 (no content) status to indicate that the item was deleted.
        """
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
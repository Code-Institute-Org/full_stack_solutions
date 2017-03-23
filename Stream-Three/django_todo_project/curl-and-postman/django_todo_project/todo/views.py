from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo


class TodoView(APIView):

    serializer_class = TodoSerializer

    def get(self, request, pk):
        if pk is not None:
            todo = Todo.objects.get(id=pk)
            serializer = TodoSerializer(todo)
        else:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

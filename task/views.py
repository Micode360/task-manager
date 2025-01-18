from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskModel
from rest_framework import status
from .serializer import TaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class TaskView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        # tasks = TaskModel.objects.filter(name__icontains="")
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"message": "Task get request successful", "data": serializer.data})
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post request successful"})
        else:
            return Response({"message": "Post request unsuccessful", "error": serializer.errors})
    
    def put(self, request, pk):
        try:
            data_in_base = TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return Response({"message": "Data doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
        
        serialzer = TaskSerializer(data_in_base, data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response({"message": "Put request successful"})
        else:
            return Response({"message": "Post request unsuccessful", "error": serialzer.errors})
    
    def delete(self, request, pk):
        try:
            data_in_base = TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return Response({"message": "Data doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        data_in_base.delete()
        return Response({"message": "Delete request successful"}, status=status.HTTP_204_NO_CONTENT)
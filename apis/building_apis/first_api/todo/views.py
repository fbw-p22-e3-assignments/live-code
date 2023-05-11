from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer


class TodoListApiView(APIView):
    """
    List all todo items using the get method.
    Create a new todo using the post method.
    """
    
    def get(self, request, *args, **kwargs):
        """
        List all the todo items
        """
        # Get all todos
        todos = Todo.objects.all()
        
        # Validate the data using the serializer
        serializer = TodoSerializer(todos, many=True)
        
        # Return data and status code
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        """
        Create a todo with given data from the request object.
        """
        
        # Create a dictionary with data passed from the request object.
        data = {
            'task': request.data.get('task'),
            'details': request.data.get('details'), 
            'completed': request.data.get('completed')
        }
        
        # Pass the data dictionary to the serializer
        serializer = TodoSerializer(data=data)
        
        # Check if data passed through serializer is valid
        if serializer.is_valid():
            
            # if data is valid save it/create new object
            serializer.save()
            
            # Return the serialized and status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # if data is not valid return errors and error code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
        
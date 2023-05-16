from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
# Permissions classes from rest_framework
from rest_framework.permissions import IsAuthenticated


class TodoListApiView(APIView):
    """
    List all todo items using the get method.
    Create a new todo using the post method.
    """
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        """
        List all the todo items
        """
        # Get all todos
        todos = Todo.objects.all()
        
        # Validate the data using the serializer
        serializer = TodoSerializer(todos, many=True)
        print(serializer.data)
        
        # Return data and status code
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        """
        Create a todo with given data from the request object.
        """
        
        # Create a dictionary with data passed from the request object.
        # data = {
        #     'task': request.data.get('task'),
        #     'details': request.data.get('details'), 
        #     'completed': request.data.get('completed')
        # }
        
        # Pass the data dictionary to the serializer
        serializer = TodoSerializer(data=request.data)
        
        # Check if data passed through serializer is valid
        if serializer.is_valid():
            
            # if data is valid save it/create new object
            serializer.save()
            
            # Return the serialized and status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # if data is not valid return errors and error code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
        
class TodoDetailApiView(APIView):
    """Lists the details for a specific todo(object)"""
    
    def get_object(self, todo_id):
        """
        Helper method to get a specific according to the passed todo_id.
        """
        try:
            # Return object specified by todo_id
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None
        
    def get(self, request, todo_id, *args, **kwargs):
        """Retrieves the todo with given ID."""
        # Retrieve object
        todo_item = self.get_object(todo_id)
        if not todo_item:
            return Response({"response": f"Object with ID #{todo_id} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)
            
        # To_do item exists
        serializer = TodoSerializer(todo_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, todo_id):
        """Updates the todo item with given ID."""
        # Retrieve object
        todo_item = self.get_object(todo_id)
        if not todo_item:
            return Response({"response": f"Object with ID #{todo_id} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Create a dictionary with data passed to the API
        # data = {
        #     'task': request.data.get('task'),
        #     'details': request.data.get('details'), 
        #     'completed': request.data.get('completed')
        # }
        
        # Create serializer instance using the TodoSerializer
        # Pass the todo_item as instance to the serializer
        # Pass the data dictionary with data to  be updated for the instance
        # Specify partial update of the fields
        serializer = TodoSerializer(instance=todo_item, data=request.data, partial=True)
        print(request.data)
        
        # Check if data is valid
        if serializer.is_valid():
            
            # Save validated data
            serializer.save()
            
            # Return appropriate response
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Return errors from the serializer and appropriate status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id):
        """Deletes an object given the todo_id"""
        # Retrieve object
        todo_item = self.get_object(todo_id)
        if not todo_item:
            return Response({"response": f"Object with ID #{todo_id} does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)
            
        # Delete object if it it exists
        todo_item.delete()
        return Response({"message": "Object successfully deleted!"}, status=status.HTTP_200_OK)
    
# TODO: Build a view for contacts
            
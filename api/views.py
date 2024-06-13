from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import CustomerSerializer
from .models import Customer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CustomerSerializer
from .models import Customer

from django.shortcuts import render
from .utils import list_urls  
from django.shortcuts import render
from django.urls import get_resolver

@api_view(['POST'])
def customer_view(request):
    """
    API(Function) view for handling customer-related operations.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: The HTTP response object.

    Raises:
        Http404: If the requested customer does not exist.

    """
    option = request.data.get('option')

    if option == 'list':
        queryset = Customer.objects.all().order_by('first_name')
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    elif option == 'create':
        # Extract values from QueryDict
        data = request.data.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')

        new_data = {'first_name': first_name,'last_name': last_name, 'date_of_birth': date_of_birth, 'excel_file':None}
        print(new_data)

        serializer = CustomerSerializer(data=new_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif option == 'retrieve':
        pk = request.data.get('first_name')
        queryset = Customer.objects.filter(first_name=pk)
        serializer = CustomerSerializer(queryset)
        return Response(serializer.data)

    elif option == 'destroy':
        pk = request.data.get('first_name')
        queryset = Customer.objects.filter(first_name=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({"error": "Invalid option"}, status=status.HTTP_400_BAD_REQUEST)


class  CustomerViewSetOpen(viewsets.ModelViewSet):
    """
    API(Class) viewset for handling customer-related operations.

    Attributes:
        queryset (QuerySet): The queryset of customers.
        serializer_class (Serializer): The serializer class for customers.

    """
    queryset = Customer.objects.all().order_by('first_name')
    serializer_class = CustomerSerializer


def list_urls():
    resolver = get_resolver()
    urls = []
    for url_pattern in resolver.url_patterns:
        urls.append(str(url_pattern.pattern))
    return urls

def handler404(request, exception):
    urls = list_urls()
    return render(request, 'available_urls.html', {'urls': urls})
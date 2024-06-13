from django.urls import include, path
# Import views from the current directory
from . import views

# Define the URL patterns for this Django application
urlpatterns = [
    # Map the 'customerslikegraph/' URL to the customer_view function in views
    path('customerslikegraph/', views.customer_view),
    
    # Map the 'customersopen/' URL to the CustomerViewSetOpen view in views
    # The view is configured to handle 'get', 'post', 'put', 'patch', and 'delete' HTTP methods
    path('customersopen/', views.CustomerViewSetOpen.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    
    # Include the URLs from the 'rest_framework' application under the 'api-auth/' URL
    # The namespace for these URLs is 'rest_framework'
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
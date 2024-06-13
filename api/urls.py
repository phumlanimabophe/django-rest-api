from django.urls import include, path
from . import views

urlpatterns = [
    path('customerslikegraph/', views.customer_view),
    path('customersopen/', views.CustomerViewSetOpen.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
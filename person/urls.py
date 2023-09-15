# from django.urls import path
# from .views import PersonCreateView, PersonDetailView

# urlpatterns = [
#     path('', PersonCreateView.as_view(), name='person-create'),
#     # path('<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
#     path('<str:identifier>/', PersonDetailView.as_view(), name='person-detail'),
#     # path('<str:name>/', PersonDetailView.as_view(), name='person-detail'),
# ]

from django.urls import path
from .views import PersonCreateView, PersonDetailView

urlpatterns = [
    path('create/', PersonCreateView.as_view(), name='person-create'),
    path('<str:identifier>/', PersonDetailView.as_view(), name='person-detail'),
]

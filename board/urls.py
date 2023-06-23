from django.urls import path

from .views import RegistrationAPIView, TaskAPIList, TaskAPIUpdate, TaskAPIDestroy

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),

    # path('api/v1/board-auth/', include('rest_framework.urls')),
]

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns =[  
      path('', views.getRoutes, name="routes"),
      path('notes/', views.getNotes, name="notes"),
      path('notes/create/', views.createNote, name="create-note"),
      path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
      path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
      path('notes/<str:pk>/', views.getNote, name="note"),
      path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('register/', views.RegisterView.as_view(), name='register'),
      path('check-username/', views.check_username, name='check_username'),

]
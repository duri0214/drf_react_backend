from django.urls import path
from . import views

urlpatterns = [
    path('', views.DailyList.as_view()),
    path('<int:pk>/', views.DailyDetail.as_view()),
    path('<str:category>/', views.DailyCategory.as_view()),
]

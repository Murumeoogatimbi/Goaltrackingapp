from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', views.GoalDetailView.as_view(), name='goal_detail'),
    path('goal/new/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goal/<int:pk>/edit/', views.GoalUpdateView.as_view(), name='goal_edit'),
    path('goal/<int:pk>/delete/', views.GoalDeleteView.as_view(), name='goal_delete'),
]
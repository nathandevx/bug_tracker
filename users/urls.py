from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
	path('list/', views.UserListView.as_view(), name='list'),
	path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
]

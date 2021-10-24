from django.urls import path
from tracker.views import tracker


app_name = 'tracker'
urlpatterns = [
	path('list/', tracker.TrackerListView.as_view(), name='list'),
	path('create/', tracker.TrackerCreateView.as_view(), name='create'),
	path('detail/<int:pk>/', tracker.TrackerDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', tracker.TrackerUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', tracker.TrackerDeleteView.as_view(), name='delete'),
]

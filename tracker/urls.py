from django.urls import path
from tracker.views import tracker


app_name = 'tracker'
urlpatterns = [
	path('list/', tracker.TrackerListView.as_view(), name='tracker-list'),
]

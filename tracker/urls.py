from django.urls import path
from tracker.views import tracker, ticket, ticket_comment


app_name = 'tracker'
urlpatterns = [
	# TRACKER
	path('list/', tracker.TrackerListView.as_view(), name='tracker-list'),
	path('create/', tracker.TrackerCreateView.as_view(), name='tracker-create'),
	path('<int:pk>/', tracker.TrackerDetailView.as_view(), name='tracker-detail'),
	path('update/<int:pk>/', tracker.TrackerUpdateView.as_view(), name='tracker-update'),
	path('delete/<int:pk>/', tracker.TrackerDeleteView.as_view(), name='tracker-delete'),

	# TICKET
	path('<int:tracker_pk>/ticket/create/', ticket.TicketCreateView.as_view(), name='ticket-create'),
	path('<int:tracker_pk>/ticket/<int:pk>/', ticket.TicketDetailView.as_view(), name='ticket-detail'),
	path('<int:tracker_pk>/ticket/update/<int:pk>/', ticket.TicketUpdateView.as_view(), name='ticket-update'),
	path('<int:tracker_pk>/ticket/delete/<int:pk>/', ticket.TicketDeleteView.as_view(), name='ticket-delete'),

	# TICKET COMMENT
	path('<int:tracker_pk>/ticket/<int:ticket_pk>/ticket-comment/create/', ticket_comment.TicketCommentCreateView.as_view(), name='ticket-comment-create'),
	path('<int:tracker_pk>/ticket/<int:ticket_pk>/ticket-comment/update/<int:pk>/', ticket_comment.TicketCommentUpdateView.as_view(), name='ticket-comment-update'),
	path('<int:tracker_pk>/ticket/<int:ticket_pk>/ticket-comment/delete/<int:pk>/', ticket_comment.TicketCommentDeleteView.as_view(), name='ticket-comment-delete'),


]

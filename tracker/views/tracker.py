from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tracker.models import Tracker
from tracker.mixins import GroupsRequiredMixin
from bug_tracker.constants import SUPERUSER, ADMIN, DEVELOPER, REQUESTER, VIEWER, PAG_BY


class TrackerListView(GroupsRequiredMixin, ListView):
	model = Tracker
	template_name = 'tracker/models/tracker/list.html'
	paginate_by = PAG_BY
	groups = [SUPERUSER, ADMIN, DEVELOPER, REQUESTER, VIEWER]
	queryset = Tracker.objects.all()


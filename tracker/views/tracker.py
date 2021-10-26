from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from tracker.models import Tracker
from tracker.mixins import GroupsRequiredMixin
from bug_tracker.constants import SUPERUSER, ADMIN, DEVELOPER, REQUESTER, VIEWER, PAG_BY
from tracker.model_forms import TrackerModelForm


class TrackerListView(GroupsRequiredMixin, ListView):
	model = Tracker
	template_name = 'tracker/models/tracker/list.html'
	groups = [SUPERUSER, ADMIN, DEVELOPER, REQUESTER, VIEWER]
	paginate_by = PAG_BY
	queryset = Tracker.objects.all()
	extra_context = {
		'model': Tracker
	}


class TrackerCreateView(GroupsRequiredMixin, CreateView):
	model = Tracker
	form_class = TrackerModelForm
	template_name = 'tracker/models/tracker/create.html'
	groups = [SUPERUSER, ADMIN]

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TrackerDetailView(GroupsRequiredMixin, DetailView):
	model = Tracker
	template_name = 'tracker/models/tracker/detail.html'
	groups = [SUPERUSER, ADMIN, DEVELOPER, REQUESTER, VIEWER]


class TrackerUpdateView(GroupsRequiredMixin, UpdateView):
	model = Tracker
	form_class = TrackerModelForm
	template_name = 'tracker/models/tracker/update.html'
	groups = [SUPERUSER, ADMIN]

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TrackerDeleteView(GroupsRequiredMixin, DeleteView):
	model = Tracker
	template_name = 'tracker/models/tracker/delete.html'
	groups = [SUPERUSER, ADMIN]

	def get_success_url(self):
		return self.model.get_list_url()

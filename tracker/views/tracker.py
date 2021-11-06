from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from bug_tracker.constants import ADMINS, ALL_GROUPS, PAG_BY
from tracker.models import Tracker, Ticket
from tracker.model_forms import TrackerModelForm
from tracker.mixins import GroupsRequiredMixin


class TrackerListView(GroupsRequiredMixin, ListView):
	model = Tracker
	template_name = 'tracker/models/tracker/list.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	extra_context = {
		'model': Tracker,
	}


class TrackerCreateView(GroupsRequiredMixin, CreateView):
	model = Tracker
	form_class = TrackerModelForm
	template_name = 'tracker/models/tracker/create.html'
	groups = ADMINS

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TrackerDetailView(GroupsRequiredMixin, DetailView):
	model = Tracker
	template_name = 'tracker/models/tracker/detail.html'
	groups = ALL_GROUPS


class TrackerUpdateView(GroupsRequiredMixin, UpdateView):
	model = Tracker
	form_class = TrackerModelForm
	template_name = 'tracker/models/tracker/update.html'
	groups = ADMINS

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TrackerDeleteView(GroupsRequiredMixin, DeleteView):
	model = Tracker
	template_name = 'tracker/models/tracker/delete.html'
	groups = ADMINS

	def get_success_url(self):
		return self.model.get_list_url()

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from bug_tracker.constants import ALL_GROUPS, ADMINS, NOT_VIEWER, PAG_BY
from tracker.models import Tracker, Ticket
from tracker.model_forms import TicketModelForm
from tracker.mixins import GroupsRequiredMixin


class TicketListView(GroupsRequiredMixin, ListView):
	model = Ticket
	template_name = 'tracker/models/ticket/list.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	extra_context = {
		'model': Ticket
	}

	def get_queryset(self):
		tracker = Tracker.objects.get(pk=self.kwargs['tracker_pk'])
		queryset = Ticket.objects.filter(tracker=tracker)
		return queryset


class TicketCreateView(GroupsRequiredMixin, CreateView):
	model = Ticket
	form_class = TicketModelForm
	template_name = 'tracker/models/ticket/create.html'
	groups = NOT_VIEWER

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		form.instance.tracker = Tracker.objects.get(pk=self.kwargs['tracker_pk'])
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TicketDetailView(GroupsRequiredMixin, DetailView):
	model = Ticket
	template_name = 'tracker/models/ticket/detail.html'
	groups = ALL_GROUPS


class TicketUpdateView(UserPassesTestMixin, UpdateView):
	model = Ticket
	form_class = TicketModelForm
	template_name = 'tracker/models/ticket/update.html'

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()

	def test_func(self):
		is_creator = self.get_object().creator == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin


class TicketDeleteView(UserPassesTestMixin, DeleteView):
	model = Ticket
	template_name = 'tracker/models/ticket/delete.html'

	def get_success_url(self):
		return Tracker.get_list_url()

	def test_func(self):
		is_creator = self.get_object().creator == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin

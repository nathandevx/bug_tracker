from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import reverse
from bug_tracker.constants import ALL_GROUPS, ADMINS, NOT_VIEWER, PAG_BY
from tracker.models import Ticket, TicketComment
from tracker.model_forms import TicketCommentModelForm
from tracker.mixins import GroupsRequiredMixin


# class TicketCommentListView(GroupsRequiredMixin, ListView):
# 	model = TicketComment
# 	template_name = 'tracker/models/ticket_comment/list.html'
# 	groups = ALL_GROUPS
# 	paginate_by = PAG_BY
# 	extra_context = {
# 		'model': TicketComment
# 	}


class TicketCommentCreateView(GroupsRequiredMixin, CreateView):
	model = TicketComment
	form_class = TicketCommentModelForm
	template_name = 'tracker/models/ticket_comment/create.html'
	groups = NOT_VIEWER

	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.instance.updater = self.request.user
		form.instance.ticket = Ticket.objects.get(pk=self.kwargs['ticket_pk'])
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()


# class TicketCommentDetailView(GroupsRequiredMixin, DetailView):
# 	model = TicketComment
# 	template_name = 'tracker/models/ticket_comment/detail.html'
# 	groups = ALL_GROUPS


class TicketCommentUpdateView(UserPassesTestMixin, UpdateView):
	model = TicketComment
	form_class = TicketCommentModelForm
	template_name = 'tracker/models/ticket_comment/update.html'

	def form_valid(self, form):
		form.instance.updater = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()

	def test_func(self):
		is_creator = self.get_object().creator == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin


class TicketCommentDeleteView(UserPassesTestMixin, DeleteView):
	model = TicketComment
	template_name = 'tracker/models/ticket_comment/delete.html'

	def get_success_url(self):
		return reverse('tracker:ticket-detail', kwargs={'tracker_pk': self.object.ticket.tracker.pk, 'pk': self.object.ticket.pk})

	def test_func(self):
		is_creator = self.get_object().creator == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin

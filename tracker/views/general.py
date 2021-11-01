from django.views.generic import TemplateView, ListView
from bug_tracker.constants import ALL_GROUPS, PAG_BY
from tracker.mixins import GroupsRequiredMixin
from tracker.models import Ticket


class Dashboard(GroupsRequiredMixin, TemplateView):
	template_name = 'tracker/general/dashboard.html'
	groups = ALL_GROUPS

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tickets'] = Ticket.objects.order_by('-votes')[:10]
		return context


class SolvedTicketListView(GroupsRequiredMixin, ListView):
	model = Ticket
	template_name = 'tracker/general/dashboard_tickets/solved.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	queryset = Ticket.objects.filter(status=Ticket.RESOLVED)


class ClosedTicketListView(GroupsRequiredMixin, ListView):
	model = Ticket
	template_name = 'tracker/general/dashboard_tickets/closed.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	queryset = Ticket.objects.filter(status=Ticket.CLOSED)


class PendingTicketListView(GroupsRequiredMixin, ListView):
	model = Ticket
	template_name = 'tracker/general/dashboard_tickets/pending.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	queryset = Ticket.objects.filter(status=Ticket.IN_PROGRESS)


class OpenTicketListView(GroupsRequiredMixin, ListView):
	model = Ticket
	template_name = 'tracker/general/dashboard_tickets/open.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY
	queryset = Ticket.objects.filter(status=Ticket.OPEN)

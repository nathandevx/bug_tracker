from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import reverse
from bug_tracker.constants import ALL_GROUPS, PAG_BY, ADMINS
from users.models import User
from users.model_forms import UserModelForm
from tracker.mixins import GroupsRequiredMixin


class UserListView(GroupsRequiredMixin, ListView):
	model = User
	template_name = 'users/list.html'
	groups = ALL_GROUPS
	paginate_by = PAG_BY

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['access'] = self.request.user.groups.filter(name__in=ADMINS).exists()
		return context


class UserDetailView(GroupsRequiredMixin, DetailView):
	model = User
	template_name = 'users/detail.html'
	groups = ALL_GROUPS


class UserUpdateView(UserPassesTestMixin, UpdateView):
	model = User
	form_class = UserModelForm
	template_name = 'users/update.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def test_func(self):
		is_creator = self.get_object() == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin


class UserDeleteView(UserPassesTestMixin, DeleteView):
	model = User
	form_class = UserModelForm
	template_name = 'users/delete.html'

	def get_success_url(self):
		return self.object.get_absolute_url()

	def test_func(self):
		is_creator = self.get_object() == self.request.user
		is_admin = self.request.user.groups.filter(name__in=ADMINS).exists()
		return is_creator or is_admin


from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.translation import gettext as _


class TimestampMixin(models.Model):
	creator = models.ForeignKey(verbose_name=_("Creator"), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_creator')
	updater = models.ForeignKey(verbose_name=_("Updater"), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_updater')
	created_at = models.DateTimeField(verbose_name=_("Date created"), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_("Date updated"), auto_now=True)

	class Meta:
		abstract = True
		# ordering = ['updated_at']
		verbose_name = _("TimestampMixin")
		verbose_name_plural = _("TimestampMixins")


class Tracker(TimestampMixin):
	title = models.CharField(verbose_name=_("Title"), default='', max_length=20)
	description = models.TextField(verbose_name=_("Description"), default='', max_length=500)

	@staticmethod
	def get_list_url():
		return reverse('tracker:tracker-list')

	@staticmethod
	def get_create_url():
		return reverse('tracker:tracker-create')

	def get_absolute_url(self):
		return reverse('tracker:tracker-detail', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('tracker:tracker-update', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('tracker:tracker-delete', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		# ordering = ['title']
		verbose_name = _("Tracker")
		verbose_name_plural = _("Trackers")


class Ticket(TimestampMixin):
	# TYPE CHOICES
	FEATURE = 'FEATURE'
	BUG = 'BUG'
	UI = 'UI'
	TYPE_CHOICES = [
		(BUG, 'Bug'),
		(UI, 'User-Interface'),
		(FEATURE, 'Feature'),
	]  # (stored, displayed)

	# status CHOICES
	OPEN = 'OPEN'
	CLOSED = 'CLOSED'
	IN_PROGRESS = 'IN PROGRESS'
	RESOLVED = 'RESOLVED'
	STATUS_CHOICES = [
		(OPEN, 'Open'),
		(CLOSED, 'Closed'),
		(IN_PROGRESS, 'In progress'),
		(RESOLVED, 'Resolved'),
	]

	# PRIORITY CHOICES
	CRITICAL = 'CRITICAL'
	HIGH = 'HIGH'
	NORMAL = 'NORMAL'
	LOW = 'LOW'
	PRIORITY_CHOICES = [
		(CRITICAL, 'Critical'),
		(HIGH, 'High'),
		(NORMAL, 'Normal'),
		(LOW, 'Low'),
	]
	title = models.CharField(verbose_name=_("Title"), default='', max_length=20)
	description = models.TextField(verbose_name=_("Description"), default='', max_length=500)
	type = models.CharField(verbose_name=_("Type"), default=BUG, max_length=11, choices=TYPE_CHOICES)
	status = models.CharField(verbose_name=_("Status"), default=OPEN, max_length=11, choices=STATUS_CHOICES)
	priority = models.CharField(verbose_name=_("Priority"), default=NORMAL, max_length=8, choices=PRIORITY_CHOICES)
	assignees = models.ManyToManyField(verbose_name=_("Assignees"), blank=True, to=settings.AUTH_USER_MODEL, related_name='assignees')
	tracker = models.ForeignKey(verbose_name=_("Tracker"), to=Tracker, on_delete=models.CASCADE)
	votes = models.IntegerField(verbose_name=_("Votes"), default=0)
	vote_profiles = models.ManyToManyField(verbose_name=_("Vote profiles"), blank=True, to=settings.AUTH_USER_MODEL, related_name='vote_profiles')
	# todo add attachment file field

	@staticmethod
	def get_list_url():
		return reverse('tracker:ticket-list')

	def get_absolute_url(self):
		return reverse('tracker:ticket-detail', kwargs={'tracker_pk': self.tracker.pk, 'pk': self.pk})

	def get_update_url(self):
		return reverse('tracker:ticket-update', kwargs={'tracker_pk': self.tracker.pk, 'pk': self.pk})

	def get_delete_url(self):
		return reverse('tracker:ticket-delete', kwargs={'tracker_pk': self.tracker.pk, 'pk': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		# ordering = ['title']
		verbose_name = _("Ticket")
		verbose_name_plural = _("Tickets")


class TicketComment(TimestampMixin):
	title = models.CharField(verbose_name=_("Title"), default='', max_length=20)
	comment = models.TextField(verbose_name=_("Comment"), default='', max_length=500)
	ticket = models.ForeignKey(verbose_name=_("Ticket"), to=Ticket, on_delete=models.CASCADE)

	@staticmethod
	def get_list_url():
		return reverse('tracker:ticket-comment-list')

	@staticmethod
	def get_create_url():
		return reverse('tracker:ticket-comment-create')

	def get_absolute_url(self):  # redirect to ticket
		return reverse('tracker:ticket-detail', kwargs={'tracker_pk': self.ticket.tracker.pk, 'pk': self.ticket.pk})

	def get_update_url(self):
		return reverse('tracker:ticket-comment-update', kwargs={{'tracker_pk': self.ticket.tracker.pk, 'ticket_pk': self.ticket.pk, 'pk': self.pk}})

	def get_delete_url(self):
		return reverse('tracker:ticket-comment-delete', kwargs={{'tracker_pk': self.ticket.tracker.pk, 'ticket_pk': self.ticket.pk, 'pk': self.pk}})

	def __str__(self):
		return self.title

	class Meta:
		# ordering = ['title']
		verbose_name = _("Ticket comment")
		verbose_name_plural = _("Ticket comments")

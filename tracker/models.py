from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class TimestampMixin(models.Model):
	creator = models.ForeignKey(verbose_name=_("Creator"), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	updater = models.ForeignKey(verbose_name=_("Updater"), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(verbose_name=_("Date created"), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_("Date updated"), auto_now=True)

	class Meta:
		abstract = True
		ordering = ['updated_at']
		verbose_name = _("TimestampMixin")
		verbose_name_plural = _("TimestampMixins")


class Tracker(TimestampMixin):
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=500)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Tracker")
		verbose_name_plural = _("Trackers")


class Ticket(TimestampMixin):
	# TYPE CHOICES
	SUGGESTION = 'SUGGESTION'
	CODE = 'CODE'
	UI = 'UI'
	TYPE_CHOICES = [
		(SUGGESTION, 'Project suggestion'),
		(CODE, 'Code'),
		(UI, 'User-Interface'),
	]  # (stored, displayed)

	# STATE CHOICES
	OPEN = 'OPEN'
	CLOSED = 'CLOSED'
	PENDING = 'PENDING'
	SOLVED = 'SOLVED'
	STATUS_CHOICES = [
		(OPEN, 'Open'),
		(CLOSED, 'Closed'),
		(PENDING, 'Pending'),
		(SOLVED, 'Solved'),
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
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=500)
	type = models.CharField(verbose_name=_("Type"), default=SUGGESTION, max_length=10, choices=TYPE_CHOICES)
	status = models.CharField(verbose_name=_("Status"), default=OPEN, max_length=10, choices=STATUS_CHOICES)
	priority = models.CharField(verbose_name=_("Priority"), default=NORMAL, max_length=10, choices=PRIORITY_CHOICES)
	assignees = models.ManyToManyField(verbose_name=_("Assignees"), to=settings.AUTH_USER_MODEL)
	tracker = models.ForeignKey(verbose_name=_("Tracker"), to=Tracker, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['priority', 'name']
		verbose_name = _("Ticket")
		verbose_name_plural = _("Tickets")


class TicketComment(TimestampMixin):
	name = models.CharField(verbose_name=_("Name"), max_length=20)
	description = models.TextField(verbose_name=_("Description"), max_length=500)
	ticket = models.ForeignKey(verbose_name=_("Ticket"), to=Ticket, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _("Ticket comment")
		verbose_name_plural = _("Ticket comments")

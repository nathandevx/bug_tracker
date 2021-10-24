from django.contrib import admin
from tracker.models import Tracker, Ticket, TicketComment

admin.site.register(Tracker)
admin.site.register(Ticket)
admin.site.register(TicketComment)

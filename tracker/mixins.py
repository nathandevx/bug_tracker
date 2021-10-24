from django.core.exceptions import PermissionDenied


class GroupsRequiredMixin:
    """
    :param groups: list of group strings
    """
    groups = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.in_groups(self.groups, request.user):
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionDenied  # if not in group
        else:
            raise PermissionDenied  # if not logged in

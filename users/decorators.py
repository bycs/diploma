from django.core.exceptions import PermissionDenied


def staff_required(function):
    """Limit view to staff only."""

    def _inner(request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return _inner


from django.http import HttpResponseForbidden

def group_required(allowed_groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You must log in first")

            if request.user.groups.filter(name__in=allowed_groups).exists():
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("Permission denied")
        return wrapper
    return decorator

from django.contrib.auth.decorators import user_passes_test
from functools import wraps

def role_required(roles=[]):
    def check_role(user):
        return user.is_authenticated and user.groups.filter(name__in=roles).exists()
    return user_passes_test(check_role)

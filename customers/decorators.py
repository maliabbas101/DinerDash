from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps


def required_roles_for_cart(allowed_roles=[]):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return func(request, *args, **kwargs)
            else:
                if request.user.groups.all()[0].name in allowed_roles:
                    return func(request, *args, **kwargs)
                else:
                    raise PermissionDenied
        return wrap
    return decorator

def required_roles(allowed_roles=[]):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            else:
                if request.user.groups.all()[0].name in allowed_roles:
                    return func(request, *args, **kwargs)
                else:
                    raise PermissionDenied
        return wrap
    return decorator



class persist_session_vars(object):
    """
    Some views, such as login and logout, will reset all session state.
    (via a call to ``request.session.cycle_key()`` or ``session.flush()``).
    That is a security measure to mitigate session fixation vulnerabilities.

    By applying this decorator, some values are retained.

    """

    def __init__(self, vars):
        self.vars = vars

    def __call__(self, view_func):

        @wraps(view_func)
        def inner(request, *args, **kwargs):
            # Backup first
            session_backup = {}
            for var in self.vars:
                try:
                    session_backup[var] = request.session[var]
                except KeyError:
                    pass

            # Call the original view
            response = view_func(request, *args, **kwargs)

            # Restore variables in the new session
            for var, value in session_backup.items():
                request.session[var] = value

            return response

        return inner

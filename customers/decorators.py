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

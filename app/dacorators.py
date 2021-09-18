from functools import wraps
from django.views.decorators.cache import cache_page

def cache_page_for_guests(*cache_args, **cache_kwargs):
    def inner_decorator(func):
        @wraps(func)
        def inner_function(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return cache_page(*cache_args, **cache_kwargs)(func)(request, *args, **kwargs)
            return func(request, *args, **kwargs)
        return inner_function
    return inner_decorator
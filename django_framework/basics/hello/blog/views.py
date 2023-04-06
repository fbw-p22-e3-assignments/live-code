from django.http import HttpResponse


def home(request):
    """The shop home view."""
    return HttpResponse('Hello from blog!')


def listing(request):
    """The shop list."""
    return HttpResponse('Browse the shop!')


def item(request, item_id):
    """A view for items."""
    return HttpResponse(f'This is {item_id}')
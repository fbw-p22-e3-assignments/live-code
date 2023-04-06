from django.http import HttpResponse


def home(request):
    """The shop home view."""
    return HttpResponse('Hello World!')


def listing(request):
    """The shop list."""
    return HttpResponse('Browse the shop!')


def item(request, item_id):
    """A view for items."""
    return HttpResponse(f'This is {item_id}')


def articles(request, month, is_int):
    """Articles for a year."""
    if is_int:
        return HttpResponse(f'{month} is an integer.')
    else:
        return HttpResponse(f'{month} is a string.')
    
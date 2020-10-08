from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as d_login
# Important for get method validate csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from movies_app.utils import *


@require_http_methods(['GET'])
@ensure_csrf_cookie
def favorites(request):
    if request.user.is_authenticated:
        favorite_movies = get_favourite_movies(request.user.id)
        return JsonResponse(favorite_movies)
    else:
        return JsonResponse({'message': 'no login available'})

@require_http_methods(['POST'])
@ensure_csrf_cookie
def favorite(request, imdb_id):
    if request.user.is_authenticated:
        message = add_favourite_movie(request.user.id, imdb_id)
        return JsonResponse(message)
    else:
        return JsonResponse({'message': 'no login available'})

@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        user = authenticate(
            request=request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            d_login(request, user)
            return JsonResponse({'message': 'Loged in'})
        else:
            return JsonResponse({'message': 'error'})
    else:
        return JsonResponse({'message': 'login page'})

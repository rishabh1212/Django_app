from django.contrib.auth import authenticate, login as d_login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


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

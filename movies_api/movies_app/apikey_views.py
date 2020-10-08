import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from movies_app.models import movie
from django.http import JsonResponse
from django.http import HttpResponse



@api_view(['GET'])
@permission_classes([HasAPIKey])
def filter_movies(request):

    search = request.GET['search']
    movie_objs = movie.objects.filter(original_title__icontains=search)
    json_pretty = json.dumps(
        {
         movie_obj.imdb_id: {'original_title': movie_obj.original_title, 'overview': movie_obj.overview}
         for movie_obj in movie_objs
        },
        sort_keys=True,
        indent=4
    )
    return HttpResponse(json_pretty,content_type="application/json")

@api_view(['GET'])
@permission_classes([HasAPIKey])
def describe_movie(request, imdb_id):
    movie_obj = movie.objects.filter(imdb_id=imdb_id)
    if movie_obj:
        return JsonResponse(
            {'imdb_id': movie_obj[0].imdb_id,
             'original_title': movie_obj[0].original_title,
             'overview': movie_obj[0].overview,
            }
        )
    return JsonResponse({'message': 'movie id does not exist'})

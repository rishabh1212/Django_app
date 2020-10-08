from movies_app.models import *


def get_favourite_movies(user_id):
	favorite_movies = userfavorites.objects.get(user__id=user_id)
	favorite_movies_dict = {}
	for movie_obj in favorite_movies.favorite_movies.all():
		favorite_movies_dict[movie_obj.imdb_id] = movie_obj.original_title
	return favorite_movies_dict

def add_favourite_movie(user_id, imdb_id):
    add_favorite, created = userfavorites.objects.get_or_create(
        user=User.objects.get(id=user_id)
    )
    movie_obj = movie.objects.filter(imdb_id=imdb_id)
    if not movie_obj:
        return {'message': 'movie id is not valid'}
    add_favorite.favorite_movies.add(*movie_obj)
    add_favorite.save()
    return {'message': 'Added to favorites'}

from django.template.response import TemplateResponse
from rest_framework.response import Response
from movies_api.models import Movies
from movies_api.serializers import MovieSerializer
from rest_framework import viewsets
import pandas as pd


class MovieViewSet(viewsets.ViewSet):
   

    def list(self, request):
        
        genre = None if not request.query_params.get('genre', '') else request.query_params.get('genre', '')
        lang = None if not request.query_params.get('lang', '') else request.query_params.get('lang', '')
        check_empty = False if len(Movies.objects.values_list()) > 0 else True


        if check_empty:

            data = pd.read_csv('imdb/static/IMDb_movies.csv')  
            movies = data.to_dict('records')
            serializer = MovieSerializer(data=movies, many=True)
            if serializer.is_valid():
                serializer.save()
                rendered_template = TemplateResponse(request, 'index.html', {'movies': serializer.data})
                return rendered_template

        elif genre != None or lang != None:
            if genre != None:
                movies = Movies.objects.filter(genre__icontains=genre.lower().capitalize())
            if lang != None:
                movies = Movies.objects.filter(language__icontains=lang.lower().capitalize())
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
            
        
        else:
            movies = Movies.objects.all()
            serializer = MovieSerializer(movies, many=True)
            rendered_template = TemplateResponse(request, 'index.html', {'movies': serializer.data})
            return rendered_template
            



 

   

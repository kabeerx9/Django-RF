from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import WatchList , StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer , StreamPlatformSerializer
from rest_framework import status


@api_view(['GET' , 'POST'])
def watch_list(request):
  if request.method == 'GET':
    movies = WatchList.objects.all()
    serializer = WatchListSerializer(movies , many=True)
    return Response(serializer.data)
  else:
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

@api_view(['GET' , 'PUT' , 'DELETE'])
def watch_detail(request,pk):
  if request.method == 'GET':
    movie = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(movie)
    return Response(serializer.data)
  elif request.method == 'PUT':
    movie = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  elif request.method == 'DELETE':
    movie = WatchList.objects.get(pk=pk)
    movie.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET' , 'POST'])
def stream_platform(request):
  if request.method == 'GET':
    platform = StreamPlatform.objects.all()
    serializer = StreamPlatformSerializer(platform , many=True )
    return Response(serializer.data)
  else:
    print("I am here with request data as ",request.data)
    serializer = StreamPlatformSerializer(data=request.data)
    print(serializer)
    print(serializer.is_valid())
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


@api_view(['GET' , 'PUT' , 'DELETE'])
def stream_detail(request,pk):
  if request.method == 'GET':
    platform = StreamPlatform.objects.get(pk=pk)
    serializer = StreamPlatformSerializer(platform)
    return Response(serializer.data)
  elif request.method == 'PUT':
    platform = StreamPlatform.objects.get(pk=pk)
    serializer = StreamPlatformSerializer(platform,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  elif request.method == 'DELETE':
    platform = StreamPlatform.objects.get(pk=pk)
    platform.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

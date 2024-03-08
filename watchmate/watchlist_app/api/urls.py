
from django.urls import path
from watchlist_app.api.views import watch_list , watch_detail , stream_platform , stream_detail

urlpatterns = [
    path("list/", watch_list, name="watch_list" ),
    path("<int:pk>" , watch_detail , name="watch_detail"),
    path("stream/", stream_platform, name="stream_platform" ),
    path("stream/<int:pk>" , stream_detail , name="stream_detail"),
]

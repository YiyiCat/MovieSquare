"""MovieSquare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from movie.views import *
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include("django.contrib.auth.urls")),
    url(r'^getMoviePoster/(.*)', getMoviePoster, name="getMoviePoster"),
    url(r'^newPost/', newPost, name="newPost"),
    url(r'^postDetail/(?P<pk>\d+)/$', PostDetailView.as_view(), name="postDetail"),
    url(r'^register/', RegisterView.as_view()),
    url(r'^getReplies/(\d+)/$', getReplies, name="getReplies"),
    url(r'^newReply/(\d+)/$', newReply, name="newReply"),
    url(r'^getMoviePosterAll/(.*)/(\d+)', getMoviePosterAll, name='getMoviePosterAll')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for folder in settings.STATIC_FOLDERS:
    urlpatterns += static("/{}/".format(folder), document_root=os.path.join(settings.BASE_DIR, folder))

"""
URL configuration for demodrf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from movies import views as mv 


# router = routers.DefaultRouter()
# router.register('movies',mv.MovieViewSet,basename='MovieData')
# router.register('action',mv.ActionViewSet,basename='action_router')

urlpatterns = [
    # path('',include(router.urls)),
    # path('api/movies',mv.MovieViewSet.as_view(),name='movie'),
    # path('api/movies',mv.get_movies,name="movies"),
    # path('api/movie_update/<int:id>/',mv.movie_update,name="movie_update"),
    path('admin/', admin.site.urls),
    path('api/',mv.MovieView.as_view(),name="movieall"),
    path('api/<int:id>/',mv.MovieView.as_view(),name="specificmovie"),
    path('logout/',mv.logout_user,name="logout"),

    path('get-token/<int:id>/',mv.GetAuthToken.as_view(),name="get-token"),
]

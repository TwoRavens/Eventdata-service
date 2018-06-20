from django.urls import path, re_path

from . import views

urlpatterns = (

    # for adding query
    #
    path(r'api/add-query',
         views.api_add_query,
         name='api_add_query'
         )
)
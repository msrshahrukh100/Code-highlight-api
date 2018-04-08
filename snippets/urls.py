from django.conf.urls import url
from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    # path(r'snippets/', views.snippet_list),
    path(r'snippets/', views.SnippetList.as_view()),
    path(r'snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path(r'users/', views.UserList.as_view()),
    path(r'users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
    path(r'api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

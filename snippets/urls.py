from django.conf.urls import url
from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    # path(r'snippets/', views.snippet_list),
    path(r'snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path(r'snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path(r'users/', views.UserList.as_view(), name="user-list"),
    path(r'users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'', views.api_root),
    path(r'snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="snippet-highlight"),

]

urlpatterns += [
    path(r'api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

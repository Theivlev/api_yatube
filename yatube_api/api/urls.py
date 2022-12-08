from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

v1_router = routers.DefaultRouter()

v1_router.register('posts', PostViewSet, basename="posts")
v1_router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
v1_router.register('groups', GroupViewSet)

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]

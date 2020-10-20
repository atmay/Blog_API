from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CommentViewSet, PostViewSet, FollowViewSet, GroupViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet,
                   basename='post')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
v1_router.register(r'group', GroupViewSet,
                   basename='group')
v1_router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),

    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

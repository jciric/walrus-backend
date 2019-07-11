from django.urls import path
from core.views import ContentViewList, ContentViewDetail, ContentViewDetailofUser

urlpatterns = [
    path("posts/", ContentViewList.as_view(), name="posts_list"),
    path("posts/<int:pk>/", ContentViewDetail.as_view(), name="posts_detail"),
    path("posts/<str:owner>/<int:pk>/", ContentViewDetailofUser.as_view(), name="posts_of_a_user" ),
]

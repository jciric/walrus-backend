# from users import views
# from django.urls import include, path
# from rest_framework import routers
#
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
from django.urls import path
from users.views import UserViewList, UserViewDetail

urlpatterns = [
    path("users/", UserViewList.as_view(), name="users_list"),
    path("users/<int:pk>/", UserViewDetail.as_view(), name="users_detail")
]

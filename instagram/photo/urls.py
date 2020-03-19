from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate

app_name = "photo"
#app_name 설정을 통해 namespace(이름공간)확보
#다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해 사용한다.

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name = 'create'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name = 'delete'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name = 'update'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name = 'detail'),
    path("", PhotoList.as_view(), name = 'index'),
]
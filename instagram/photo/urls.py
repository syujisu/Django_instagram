from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate, PhotoLike, PhotoFavorite
from django.conf.urls.static import static
from django.conf import settings
from .models import Photo


app_name = "photo"
#app_name 설정을 통해 namespace(이름공간)확보
#다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해 사용한다.

urlpatterns = [
    path(r"create/", PhotoCreate.as_view(), name = 'create'),
    path(r"delete/<int:pk>/", PhotoDelete.as_view(), name = 'delete'),
    path(r"update/<int:pk>/", PhotoUpdate.as_view(), name = 'update'),
    path(r"detail/<int:pk>/", PhotoDetail.as_view(), name = 'detail'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/", PhotoFavorite.as_view(), name='favorite'),
    path("", PhotoList.as_view(), name = 'index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
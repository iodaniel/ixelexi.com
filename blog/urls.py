from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='news'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
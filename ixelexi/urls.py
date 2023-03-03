from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from ixelexi.sitemaps import MySitemap
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'static': MySitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),

    path('blog', include('blog.urls')),
    path('', include('booking.urls')),
    path('user', include('app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  



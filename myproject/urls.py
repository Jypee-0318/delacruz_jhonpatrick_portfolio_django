from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('portfolio/', include('portfolio.urls', namespace="portfolio")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
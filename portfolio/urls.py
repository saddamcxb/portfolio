from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('homepage.urls')),
    path("blog/", include("blog.urls")),
    path("skill/", include("skills.urls")),
    path("project/", include("project.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




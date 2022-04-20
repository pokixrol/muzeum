from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from muzeum import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('exemplar/', include('exemplar.urls')),
                  path('', RedirectView.as_view(url='exemplar/'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)

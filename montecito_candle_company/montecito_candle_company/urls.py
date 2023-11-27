# montecito_candle_company/urls.py
from django.contrib import admin
from django.urls import path, include
from store.views import index  # Import the index view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', index, name='index'),  # Add the index view for the root path
    # Add other URL patterns as needed
  # Include the URLs of your 'store' app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



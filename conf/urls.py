from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Welcome to my API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),
    path('api/leader/', include('leader.urls')),
    path('api/connect/', include('connect.urls')),
    path('api/news/', include('news.urls')),
    path('api/project/', include('project.urls')),
    path('api/account/', include('accounts.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

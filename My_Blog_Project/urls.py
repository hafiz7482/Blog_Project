from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns   # Static files er jonno
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_login.urls')),
    path('blog/', include('App_blog.urls')),
    path('', views.Index, name='index')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
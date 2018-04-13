from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import qtsp_solver.views

# Examples:
# url(r'^$', 'app_settings.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', qtsp_solver.views.index, name='index'),
    url(r'^db', qtsp_solver.views.db, name='db'),
    path('admin/', admin.site.urls),
]

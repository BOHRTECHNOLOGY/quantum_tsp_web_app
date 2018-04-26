from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

import qtsp_solver.views
import qtsp_solver.controller

# Examples:
# url(r'^$', 'app_settings.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', qtsp_solver.views.index, name='index'),
    url(r'^db', qtsp_solver.views.db, name='db'),
    url(r'^get_result', csrf_exempt(qtsp_solver.controller.schedule_job)),
    path('admin/', admin.site.urls),
]

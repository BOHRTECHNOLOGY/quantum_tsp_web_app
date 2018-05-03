from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

import qtsp_solver.views
import qtsp_solver.controller


urlpatterns = [
    url(r'^$', qtsp_solver.views.index, name='index'),
    url(r'^schedule_job', csrf_exempt(qtsp_solver.controller.schedule_job)),
    url(r'^get_result', csrf_exempt(qtsp_solver.controller.get_result)),
    path('admin/', admin.site.urls),
]

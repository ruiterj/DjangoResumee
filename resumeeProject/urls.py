from django.urls import path
from resumeeApp import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('templates/', views.templates, name='templates'),
    path('builder/', views.builder, name='builder'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('set-template-color/', views.set_template_color, name='set_template_color'),
    path('render-resume-preview/', views.render_resume_preview, name='render_resume_preview'),
    path('resume/<int:resume_id>/', views.resume_detail, name='resume_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
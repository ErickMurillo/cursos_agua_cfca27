from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CourseListView.as_view(), name="list_course"),
    url(r'^(?P<slug>[-\w]+)/$', views.CourseDetailView.as_view(), name="detail_course"),
    url(r'^seguir/(?P<id>[-\w]+)/$/', views.seguir_curso, name='seguir_curso'),
	url(r'^dejar/seguir/(?P<id>[-\w]+)/$/', views.dejar_seguir_curso, name='dejar_seguir_curso'),
]

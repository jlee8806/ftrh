from django.conf.urls import url
from . import views

# from .views import(
# 	list,
# 	create,
# 	detail,
# 	update,
# 	delete,
# 	)


urlpatterns = (
	url(r'^$', "apps.games.views.list", name='list'),
	url(r'^create/$', "apps.games.views.create"),
	url(r'^(?P<id>\d+)/$', "apps.games.views.detail", name='detail'),
	url(r'^(?P<id>\d+)/edit/$', "apps.games.views.update", name='update'),
	url(r'^(?P<id>\d+)/delete/$', "apps.games.views.delete"),




	)
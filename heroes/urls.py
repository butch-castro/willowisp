from django.conf.urls import url

from .views import HomeView, CloudView, SunfloweyView, JesterView

urlpatterns = [
	url(r'^heroes$', HomeView.as_view(), name='heroes'),
	url(r'^hero/cloud$', CloudView.as_view(), name='cloud'),
	url(r'^hero/sunflowey$', SunfloweyView.as_view(), name='sunflowey'),
    url(r'^hero/jester$', JesterView.as_view(), name='jester')
]
from django.conf.urls import patterns, url
from home.views import CountDownView

urlpatterns = patterns('', 
	url(r'^$', CountDownView.as_view(), name='home'),
)
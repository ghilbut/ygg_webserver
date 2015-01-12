from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^$', 'webserver.index'),
	
    url(r'^api/reg/localbox/proxy/address$', 'webserver.apps.api.views.reg_localbox_proxy_address'),
    url(r'^api/unreg/localbox/proxy/address$', 'webserver.apps.api.views.unreg_localbox_proxy_address'),

    url(r'^test/localbox/proxy/address$', 'webserver.apps.test.views.test_localbox_proxy_address'),
)

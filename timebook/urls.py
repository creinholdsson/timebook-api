from django.conf.urls import patterns, url, include

urlpatterns = patterns('timebook.views',
                       url(r'^customers/$', 'customer_list'),
                       url(r'^customers/(?P<pk>[0-9]+)/$', 'customer_detail'),
                       url(r'^jobs/$', 'job_list'),
                       url(r'^jobs/(?P<pk>[0-9]+)/$', 'job_detail'),
                       url(r'^workers/$', 'worker_list'),
                       url(r'^workers/(?P<pk>[0-9]+)/$', 'worker_detail'),
                       url(r'^timetypes/$', 'timetype_list'),
                       url(r'^timetypes/(?P<pk>[0-9]+)/$', 'timetype_detail'),
                       url(r'^times/$', 'time_list'),
                       url(r'^times/(?P<pk>[0-9]+)/$', 'time_detail'),
                       )

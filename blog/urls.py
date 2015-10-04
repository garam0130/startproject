from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
	url(r'^add/$', 'group_add', name='group_add'),
    url(r'^$', 'group_list', name='group_list'),
    url(r'^pre_group/$', 'pre_group_list', name='pre_group_list'),
    url(r'^ing_group/$', 'ing_group_list', name='ing_group_list'),
    url(r'^complete_group/$', 'complete_group_list', name='complete_group_list'),
    url(r'^(?P<pk>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', 'edit', name="edit"),
    url(r'^(?P<pk>\d+)/delete/$', 'delete', name="delete"),
    url(r'^(?P<pk>\d+)/comments/new/$', 'comment_new', name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'comment_edit', name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'comment_delete', name='comment_delete'),
    url(r'^applicant_list/$', 'applicant_list', name='applicant_list'),
    url(r'^applicant_approve/$', 'applicant_approve', name='applicant_approve'),
)


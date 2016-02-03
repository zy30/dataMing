from django.conf.urls import url
from . import views
app_name = 'dataming'
urlpatterns = [
    url(r'^$',views.dataming_index, name='index'),
	url(r'^label/$',views.dataming_label,name='label'),
	url(r'^label/(?P<article_id>[0-9]+)/$',views.dataming_label_detail,name='label_detail'),
	url(r'^label/result/(?P<article_id>[0-9]+)/$',views.dataming_label_result,name='label_result'),
	url(r'^label/submit/(?P<article_id>[0-9]+)/$',views.submit,name='submit'),

]

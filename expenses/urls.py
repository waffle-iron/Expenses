from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manage_operations/$', views.manage_operations, name='manage_operations'),
    url(r'^new_operation/$', views.new_operation, name='new_operation'),
    url(r'^manage_categories/$', views.manage_categories, name='manage_categories'),
    url(r'^new_category/$', views.new_category, name='new_category'),
    url(r'^manage_accounts/$', views.manage_accounts, name='manage_accounts'),
    url(r'^new_account/$', views.new_account, name='new_account')
]

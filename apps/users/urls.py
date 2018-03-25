from django.conf.urls import url

from apps.users import views


urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    # url(r'^do_register', views.do_register, name='do_register'),

    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^active/(.+)$', views.ActiveView.as_view(), name='active'),

]

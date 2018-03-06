from django.conf.urls import url
from AppTwo import views

app_name = 'AppTwo_myurlvar'

urlpatterns = [

    url(r'^user',views.UserView,name='user_myurl'),
    url(r'^help/',views.help,name='helpinmyurl'),
    url(r'^rel',views.relativeView,name='myurl_rel'),
    url(r'^register',views.registrationView,name='reg_myurl'),
    ]

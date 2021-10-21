from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns =[
        path('',views.homepage,name='homepage'),
        path('post/<str:pk>',views.blogpost,name='blogpost'),
        path('about/',views.about,name='about'),
        #path('signup/',views.signup,name='signup'),
        path('contact/',views.contact,name='contact'),
        #path('login/',views.Login,name='Login')
        path('add_post/',views.create_view, name = 'create_view'),
        path('list_post/',views.list_view, name = 'list_view'),
        path('update_post/<str:pk>',views.update_post,name='update_post'),
        path('delete_post/<str:pk>',views.delete_view,name='delete_post'),
        path('translate/',views.translator,name='translator')




]
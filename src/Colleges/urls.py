from django.urls import path
from . import views


urlpatterns = [
	
	path('',views.home, name='home'),
	path('nits/',views.nits, name='nits'),
	path('iits/',views.iits, name = 'iits'),
	path('contact/',views.contact, name='contact'),
	path('about/', views.about, name='about'),
]
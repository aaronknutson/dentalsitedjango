from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('pricing/', views.pricing, name="pricing"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog-details"),
    path('booking_now/', views.booking_now, name="booking-now"),
    path('appointment/', views.appointment, name="appointment"),
]

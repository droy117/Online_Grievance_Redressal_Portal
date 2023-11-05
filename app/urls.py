from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register_grievance", views.register_grievance, name="register_grievance"),
    path("track_grievance", views.track_grievance, name="track_grievance"),
    path("lodge_grievance", views.lodge_grievance, name="lodge_grievance"),
    path("escalate", views.escalate, name="escalate"),
    path("grievance_detail/<int:ref_no>", views.grievance_detail, name="grievance_detail"),
    path("handler_response/<int:ref_no>", views.handler_response, name="handler_response"),
    path("satisfied_fn/<int:ref_no>", views.satisfied_fn, name="satisfied_fn"),
]
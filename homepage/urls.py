from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path("contact/", views.contact_view, name='contact'),
    path("education/", views.education, name="education"),
    path("links/", views.profile, name='profile'),
]


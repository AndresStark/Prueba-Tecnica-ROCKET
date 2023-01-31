from django.urls import path
from . import views

app_name = "prueba"
urlpatterns = [
    # ex: /prueba/
    path("", views.IndexView.as_view(), name="index"),
    path("detail/", views.DetailView.as_view(), name="detail"),
]
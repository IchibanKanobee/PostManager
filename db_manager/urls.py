from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_platform", views.add_platform, name="add_platform"),
    path("add_record_type", views.add_record_type, name="add_record_type"),
    path("add_record", views.add_record, name="add_record"),
    path("add_account", views.add_account, name="add_account"),
    path("add_post", views.add_post, name="add_post"),
]
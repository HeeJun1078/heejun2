from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("study", views.study, name="test"),
    path("sleep", views.sleep, name="sleep"),
    path("question/<int:qid>/", views.question, name="question"),
    path("add/<int:a>/<int:b>/", views.add),
    path("mul/<int:a>/<int:b>/", views.mul),
]
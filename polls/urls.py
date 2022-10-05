from django.urls import path

from . import views

urlpatterns = [
    path('', views.getdata, name='getdata'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/results/', views.results, name='results'),
]
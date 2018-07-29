from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #path('test', views.Simple_Interface.as_view(), name='Simple_Interface'),
    path('post', views.Simple_Interface.as_view(), name='Simple_Interface'),
    path('login', views.Login.as_view(), name='Login'),
    path('home', views.HomeView.as_view(), name='home'),
    path('list', views.IndexView.as_view(), name='List'),
    #path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('post/submit/', views.submit, name='submit'),
    path('post/authenticate', views.userauthentication, name='authenticate'),
    #path('<int:pk>/post_results/', views.ResultsView.as_view(), name='results'),
    #path('test/postQ/', views.postQ, name='postQ'),
]
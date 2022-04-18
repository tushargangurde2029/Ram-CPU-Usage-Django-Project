from django.urls import path
from . import views

urlpatterns = [
    #path('',views.hello,name="hello")
    path('', views.HomeView.as_view()),
    # path('test-api', views.get_data),
    path('api', views.ChartData.as_view()),
]
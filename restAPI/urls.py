from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test', views.PostList.as_view()),
    path('test/<int:pk>/', views.PostDetail.as_view()),
]
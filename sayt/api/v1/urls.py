from django.urls import path

from api.v1.Category.views import CategoryView
from api.v1.News.views import NewsView
from api.v1.user.views import AuthView

urlpatterns = [
    path('ctg/list/', CategoryView.as_view(), name='ctg_list'),
    path('ctg/list/<int:pk>/', CategoryView.as_view(), name='ctg_one'),

    path('news/', NewsView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsView.as_view(), name='news_one'),

    path('auth/register/', AuthView.as_view(), name="api_register"),
]
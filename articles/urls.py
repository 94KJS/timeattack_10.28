from django.urls import path
from articles import views


urlpatterns = [
    path('api/article',views.ArticleView.as_view(), name="article_view")
]
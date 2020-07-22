from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('articleVS', ArticleViewset, basename='article')
router.register('articleGVS', GenericArticle, basename='GenericArticle')

urlpatterns = [
    path('article/', article_list ),
    path('article/<int:pk>' ,article_detail),
    path('articleView/' ,ApiViewArticle.as_view()),
    path('articleView/<int:id>' ,ApiViewArticleUD.as_view()),
    path('articleGeneric/', GenericApi.as_view()),
    path('articleGeneric/<int:id>', GenericApi.as_view()),
    path('VS/', include(router.urls)),
    path('GVS/', include(router.urls))
]
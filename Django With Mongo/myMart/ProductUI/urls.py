from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('items', ProductDetail, basename='products')
router.register('specs',SpecsDetails, basename='specifications')
router.register('reviews',UserReviewDetails, basename='userreview')

urlpatterns = [
path('api/', include(router.urls)),
path('api/userreview/', getUserReview, name='UserReview'),
path('api/upvote/<int:id>', handleUpvotes, name='upvotes'),
path('api/search', Search, name='search')
]


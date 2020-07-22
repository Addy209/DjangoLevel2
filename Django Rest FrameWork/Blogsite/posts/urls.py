from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('postVS',GenericPostDB)
router.register('draftVS', DraftListApi)
router.register('testVS', DraftListApi)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about' ),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', CreatePostView.as_view(), name='post_new'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='post_remove'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('comment/<int:pk>', add_comment_to_post, name='comment'),
    path('approve_comments/<int:pk>', approve_comment, name='approve_comment'),
    path('remove_comment/<int:pk>', remove_comment, name='remove_comment'),
    path('post_publish/<int:pk>', publish_post, name='publish_post'),
    path('GVS/', include(router.urls)),
    path('API/publish/<int:pk>',publish_post)

]
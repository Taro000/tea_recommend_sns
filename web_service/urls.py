from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register('user-profiles', UserProfileViewSet, 'user_profiles')
router.register('teas', TeaViewSet, 'teas')
router.register('evaluations', EvaluationViewSet, 'evaluations')
router.register('preferences', PreferenceViewSet, 'preferences')
router.register('posts', PostViewSet, 'posts')


urlpatterns = [
    path('', include(router.urls)),
]
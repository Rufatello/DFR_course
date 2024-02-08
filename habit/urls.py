from django.urls import path
from rest_framework.routers import DefaultRouter
from habit.apps import HabitConfig
from habit.views import HabitViewSet, ReflexAPIView, ReflexCreateApiView, ReflexDestroyAPIView, ReflexUpdateAPIView, \
    ReflexListUserdAPIView

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')


urlpatterns = [
    path('reflex/list/', ReflexAPIView.as_view(), name='habit-list'),
    path('reflex/create/', ReflexCreateApiView.as_view(), name='create-reflex'),
    path('reflex/<int:pk>/delete/', ReflexDestroyAPIView.as_view(), name='lesson-delete'),
    path('reflex/<int:pk>/update/', ReflexUpdateAPIView.as_view(), name='lesson-update'),
    path('reflex/list/user/', ReflexListUserdAPIView.as_view(), name='detail-reflex')


]+router.urls
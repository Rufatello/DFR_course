from django.shortcuts import render
from rest_framework import viewsets, status, generics

from habit.models import Habit, Reflex
from habit.paginations import ReflexPagination
from habit.serializers import HabitSerializer, ReflexSerializer, ReflexDetailSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class ReflexListUserdAPIView(generics.ListAPIView):
    serializer_class = ReflexSerializer
    pagination_class = ReflexPagination

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)


class ReflexAPIView(generics.ListAPIView):
    serializer_class = ReflexDetailSerializer
    queryset = Reflex.objects.filter(is_publicity=True)


class ReflexCreateApiView(generics.CreateAPIView):
    serializer_class = ReflexSerializer

    # def perform_create(self, serializer):
    #     new_lesson = serializer.save()
    #     new_lesson.user = self.request.user
    #     new_lesson.save()


class ReflexUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ReflexSerializer
    queryset = Reflex.objects.all()

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)


class ReflexDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ReflexSerializer
    queryset = Reflex.objects.all()

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)




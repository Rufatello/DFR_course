from rest_framework import serializers

from habit.models import Habit, Reflex
from habit.validators import ValidatorTime


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'


class ReflexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflex
        fields = '__all__'
        validators = [ValidatorTime.validator_time]



class ReflexDetailSerializer(serializers.ModelSerializer):
    habit = HabitSerializer(read_only=True)

    class Meta:
        model = Reflex
        fields = '__all__'


from rest_framework.serializers import ValidationError


# class Validation:
#     def validate_nice_reflex(data):
#         if data['nice_reflex'] == True and (data['fee'] or data['habit']):
#             raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class ValidatorTime:
    def validator_time(data):
        if data['time_to_complete'] > 120:
            raise ValidationError('Время не может быть больше 120 секунд')


# class ValidatorFee:
#     def validator_fee(data):
#         if data['fee'] and data['habit']:
#             raise ValidationError('Нельзя связать привычку и указать вознагрождение')





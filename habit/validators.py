from rest_framework.serializers import ValidationError
import re



class Validator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        if value.get(self.fields[0]):
            value['fee'] = None
        return value




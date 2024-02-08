from rest_framework.serializers import ValidationError
import re



class Validator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        value['fee'] = None
        value['habit'] = None
        return value




from django.core.exceptions import ValidationError


# from django.core.validators import validate_email


def mobile_validator(mobile):
    if mobile[0:2] != '09':
        raise ValidationError('Please follow the mentioned format')


def mobile_length_validator(mobile):
    if len(mobile) != 11:
        raise ValidationError('Please follow the mentioned format:invalid length')


def validate_not_empty(value):
    if value == '':
        raise ValidationError('{} is empty!'.format(value))

# def email_validator(email):
#     if validate_email(email):
#         raise ValidationError("Enter a valid e-mail address.")

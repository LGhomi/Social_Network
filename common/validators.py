from django.core.exceptions import ValidationError
import re


def mobile_validator(mobile):
    """

    :param mobile:User mobile number
    :return: Checks mobile number must start with 09
    """
    if mobile[0:2] != '09':
        raise ValidationError('Please follow the mentioned format')


def mobile_length_validator(mobile):
    """

    :param mobile: User mobile number
    :return: The mobile number must be 11 digits
    """
    if len(mobile) != 11:
        raise ValidationError('Please follow the mentioned format:invalid length')


def validate_not_empty(value):
    """

    :return:Checks if the field is empty
    """
    if value == '':
        raise ValidationError('{} is empty!'.format(value))


def email_validator(email):
    """

    :param email: User email
    :return: Implements more restrictions on email validity using Regex
    """
    EMAIL_REGEX = re.compile(r'^[a-z]+[a-zA-Z0-9.+_-]*@[a-zA-Z0-9]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(email):
        raise ValidationError('Invalid Email Address!')

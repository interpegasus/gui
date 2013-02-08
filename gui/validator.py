from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)

def validate_cpu(value):
    if value < 2 or value > 32:
        raise ValidationError(u'%s is not in range 2 - 32' % value)

def validate_memory(value):
    if value < 2 or value > 512:
        raise ValidationError(u'%s is not in range 2 - 512' % value)
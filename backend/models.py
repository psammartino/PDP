from django.db import models


class RiskType(models.Model):

    name = models.CharField(max_length=100)


class Field(models.Model):

    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    ENUM = 'enum'

    TYPE_CHOICES = (
        (TEXT, TEXT.capitalize()),
        (NUMBER, NUMBER.capitalize()),
        (DATE, DATE.capitalize()),
        (ENUM, ENUM.capitalize()),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name='fields')

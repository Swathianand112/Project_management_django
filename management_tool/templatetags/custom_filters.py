from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def calculate_age(date_of_birth):
    if date_of_birth:
        return now().year - date_of_birth.year
    return None

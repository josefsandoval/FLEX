from django import template

from app.models import UserProfile

register = template.Library()

# returns percentage between two numbers
@register.filter
def as_percentage_of(x, y):
    try:
        return "%d%%" % (float(x) / y * 100)
    except (ValueError, ZeroDivisionError):
        return ""


# returns the intersection of two sets
@register.filter
def intersect_activities(current_user, other_user):
    return list(set(current_user) & set(other_user))
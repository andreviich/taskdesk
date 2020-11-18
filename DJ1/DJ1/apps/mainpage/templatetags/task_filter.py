from django import template
from django.apps import apps
Task = apps.get_model('subjects', 'Task')

register = template.Library()
@register.filter
def filter_tasks(value, arg):
    """Removes all values of arg from the given string"""
    return Task.objects.filter(subject_id = arg)

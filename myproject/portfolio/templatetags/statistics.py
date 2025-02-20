from django import template

register = template.Library()

@register.filter
def format_count(value):
    try:
        return "${:,.2f}".format(float(value))
    except (ValueError, TypeError):
        return value
from django import template

register = template.Library()

@register.filter
def to(value, arg):
    """
    Usage: {% for i in 1|to:20 %}
    Generates numbers from value (1) to arg (20) inclusive.
    """
    try:
        start = int(value)
        end = int(arg)
        if start <= end:
            return range(start, end + 1)
        else:
            return range(start, end - 1, -1)
    except Exception:
        return []

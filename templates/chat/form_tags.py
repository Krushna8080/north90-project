from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    """
    Template filter to add CSS classes to form fields.
    Usage: {{ form.field|addclass:"css-class-name" }}
    """
    return field.as_widget(attrs={"class": css})
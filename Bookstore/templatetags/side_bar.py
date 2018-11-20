from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def selectSideButton(request, urls):
    path = request.path.split('/')[1]
    if path in (url for url in urls.split()):
        return 'sideButtonSelected'
    return 'sideButton'

@register.simple_tag
def selectSideLabel(request, urls):
    path = request.path.split('/')[1]
    if path in (url for url in urls.split()):
        return 'sideButtonLabelSelected'
    return 'sideButtonLabel'

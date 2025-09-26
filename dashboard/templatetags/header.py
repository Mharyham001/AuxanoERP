from django.template import Library
from dashboard.models import SiteSetting

register = Library() 

@register.inclusion_tag('dashboard.html') 
def header_view(request):
    branding = SiteSetting.objects.first()
    if branding:
        color = branding.color
    else:
        color = None
 
    context = {
        'request' : request,
        'color' : color,
    }
    return context

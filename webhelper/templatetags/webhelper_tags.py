from webhelper.models import SocialLinks, OfficeAddress, RegisterAddress, GeneralInfo
from django.contrib.sites.models import get_current_site
from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_social_link(context, sociallink):
    '''
        ...
        {% load webhelper %}
        ...

        {% get_social_link 'facebook' %}
        {% get_social_link 'database field from SocialLins model' %}

    '''
    request = context['request']
    domain = get_current_site(request)
    try:
        link = SocialLinks.objects.get(site=domain)
        if sociallink in link._meta.get_all_field_names():
            return getattr(link, sociallink)
        else:
            return 'Invalid context'
    except SocialLinks.DoesNotExist:
        return 'Invalid context'


@register.assignment_tag(takes_context=True)
def get_office_address(context):
    '''
        ...
        {% load webhelper %}
        ...

        {% get_office_address as address %}
        {{ address.name }}
        {{ address.country }}
        {{ address.state }}
        {{ address.city }}
        {{ address.address }}
    '''
    request = context['request']
    domain = get_current_site(request)
    try:
        address = OfficeAddress.objects.get(site=domain)
    except OfficeAddress.DoesNotExist:
        address = None
    return address


@register.assignment_tag(takes_context=True)
def get_register_address(context):
    '''
        ...
        {% load webhelper %}
        ...

        {% get_register_address as address %}
        {{ address.name }}
        {{ address.country }}
        {{ address.state }}
        {{ address.city }}
        {{ address.address }}
    '''
    request = context['request']
    domain = get_current_site(request)
    try:
        address = RegisterAddress.objects.get(site=domain)
    except RegisterAddress.DoesNotExist:
        address = None
    return address


@register.assignment_tag(takes_context=True)
def get_general_info(context, ask_for):
    '''
        ...
        {% load webhelper %}
        ...

        {% get_general_info 'phone_1' %}
        {% get_general_info 'phone_2' %}
        {% get_general_info 'phone_3' %}
        {% get_general_info 'tollfree' %}
        {% get_general_info 'supprt_email' %}
        {% get_general_info 'sales_email' %}
        {% get_general_info 'Billing_email' %}
        {% get_general_info 'Website' %}
    '''
    request = context['request']
    domain = get_current_site(request)
    try:
        info = GeneralInfo.objects.get(site=domain)
        if ask_for in info._meta.get_all_field_names():
            return getattr(info, ask_for)
    except:
        return 'Define this value from admin page'

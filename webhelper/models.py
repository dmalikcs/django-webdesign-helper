from django.db import models
from django.contrib.sites.models import Site
from django.core.validators  import RegexValidator


class SocialLinks(models.Model):
    '''
    facebook
    linkedin
    twitter
    gluse
    rss
    '''
    facebook = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    linkedin = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    twitter = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    gpluse = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    rss = models.URLField(
        max_length=100,
        blank=True,
        null=True
    )
    site = models.OneToOneField(Site)

    class Meta:
        verbose_name = 'Social Links'
        verbose_name_plural = 'Soical Links'

    def __unicode__(self):
        return self.site.domain


class BaseAddress(models.Model):
    '''
    BaseAddress model extend in OfficeAddress/RegisterAddress
    '''
    name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    street_1 = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    street_2 = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    site = models.OneToOneField(Site)

    class Meta:
        abstract = True


class RegisterAddress(BaseAddress):
    class Meta:
        verbose_name = 'Register Address'
        verbose_name_plural = 'Register Address'

    def __unicode__(self):
        return self.name


class OfficeAddress(BaseAddress):
    class Meta:
        verbose_name = 'office Address'
        verbose_name = 'office Address'

    def __unicode__(self):
        return self.name


class GeneralInfo(models.Model):
    phone_1 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r'^[-\d+]+$',
                'Enter the valid phone number'
            ),
        ]
    )
    phone_2 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r'^[-\d+]+$',
                'Enter the valid phone number'
            ),
        ]
    )
    phone_3 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r'^[-\d+]+$',
                'Enter the valid phone number'
            ),
        ]
    )
    fax = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r'^[-\d+]+$',
                'Enter the valid Fax number'
            ),
        ]
    )
    tollfree = models.CharField(
        max_length=11,
        blank=True,
        null=True
    )
    support_email = models.EmailField(
        blank=True,
        null=True
    )
    sales_email = models.EmailField(
        blank=True,
        null=True
    )
    Billing_email = models.EmailField(
        blank=True,
        null=True
    )
    Website = models.URLField()
    site = models.OneToOneField(Site)

    class Meta:
        verbose_name = 'general Info'
        verbose_name_plural = 'general infos'

    def __unicode__(self):
        return self.site.domain

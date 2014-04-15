from django.test import TestCase
from django.test.client import Client
from webhelper.models import SocialLinks, RegisterAddress, OfficeAddress, GeneralInfo
from django.core.urlresolvers import reverse
from webhelper.templatetags import webhelper_tags


class WebDesign(TestCase):

    FACEBOOK_URL = 'http://facebook/dmallikcs'
    LINKED_URL = 'http://linkedin.com/in/dmalikcs'
    TWITTER_URL = 'http://twitter.com/dmalikcs'
    GPLUS_URL = 'http://google.com/dmalikcs'

    BASE_NAME = 'Deepak Malik'
    BASE_STREET_1 = 'Nehru Market'
    BASE_STREET_2 = 'Nehru Market'
    BASE_COUNTRY = 'India'
    BASE_CITY = 'Dehradun'

    PHONE_1 = 9898
    PHONE_2 = 9898
    PHONE_3 = 9898
    TOLLFREE = 800800
    SUPPORT_EMAIL = 'support@krunksystems.com'
    BILLING_EMAIL = 'billing@krunksystems.com'
    SALES_EMAIL = 'sales@krunksystems.com'

    def setUp(self):
        self.client = Client()
        self.sociallink = SocialLinks.objects.create(
            facebook=self.FACEBOOK_URL,
            linkedin=self.LINKED_URL,
            twitter=self.TWITTER_URL,
            gpluse=self.GPLUS_URL,
            site_id=1
        )
        self.registeradd = RegisterAddress.objects.create(
            name=self.BASE_NAME,
            street_1=self.BASE_STREET_1,
            street_2=self.BASE_STREET_2,
            country=self.BASE_COUNTRY,
            city=self.BASE_CITY,
            site_id=1
        )

        self.officeadd = OfficeAddress.objects.create(
            name=self.BASE_NAME,
            street_1=self.BASE_STREET_1,
            street_2=self.BASE_STREET_2,
            country=self.BASE_COUNTRY,
            city=self.BASE_CITY,
            site_id=1
        )
        self.geninfo = GeneralInfo.objects.create(
            phone_1=self.PHONE_1,
            phone_2=self.PHONE_2,
            phone_3=self.PHONE_3,
            tollfree=self.TOLLFREE,
            support_email=self.SUPPORT_EMAIL,
            Billing_email=self.BILLING_EMAIL,
            sales_email=self.SALES_EMAIL,
            site_id=1
        )

    def test_links(self):
        self.assertEqual(self.sociallink.facebook, self.FACEBOOK_URL)
        self.assertEqual(self.sociallink.linkedin, self.LINKED_URL)
        self.assertEqual(self.sociallink.twitter, self.TWITTER_URL)
        self.assertEqual(self.sociallink.gpluse, self.GPLUS_URL)

    def test_response(self):
        self.url = reverse('webhelper-home')
        self.assertEqual(self.url, '/webhelper/')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_address(self):
        self.url = reverse('webhelper-home')
        response = self.client.get(self.url)
        self.assertContains(response, 'Address', status_code=200)
        self.assertContains(response, 'facebook', status_code=200)
        self.assertContains(response, 'linkedin', status_code=200)

    def test_template_tags(self):
        client = self.client.get('/webhelper/')
        response = webhelper_tags.get_social_link(client.context, 'facebook')
        self.assertEqual(response, self.FACEBOOK_URL)
        # Wrong context
        response = webhelper_tags.get_social_link(client.context, 'faceboo')
        self.assertEqual(response, 'Invalid context')
        response = webhelper_tags.get_office_address(client.context)
        self.assertEqual(response.name, self.BASE_NAME)
        response = webhelper_tags.get_register_address(client.context)
        self.assertEqual(response.name, self.BASE_NAME)
        phone_1 = webhelper_tags.get_general_info(client.context, 'phone_1')
        self.assertEqual(phone_1, self.PHONE_1)

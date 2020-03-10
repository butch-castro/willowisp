from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/heroes')
        self.assertTemplateUsed(response, 'heroes.html')


class CloudPageTest(TestCase):

    def test_cloud_page_returns_correct_html(self):
        response = self.client.get('/hero/cloud')
        self.assertTemplateUsed(response, 'detail_cloud.html')


class SunfloweyPageTest(TestCase):

    def test_sunflowey_page_returns_correct_html(self):
        response = self.client.get('/hero/sunflowey')
        self.assertTemplateUsed(response, 'detail_sunflowey.html')


class JesterPageTest(TestCase):
    
    def test_jester_page_returns_correct_html(self):
        response = self.client.get('/hero/jester')
        self.assertTemplateUsed(response, 'detail_jester.html')
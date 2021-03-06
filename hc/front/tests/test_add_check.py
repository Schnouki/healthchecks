from django.contrib.auth.models import User
from django.test import TestCase
from hc.api.models import Check


class AddCheckTestCase(TestCase):

    def setUp(self):
        self.alice = User(username="alice")
        self.alice.set_password("password")
        self.alice.save()

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice", password="password")
        r = self.client.post(url)
        assert r.status_code == 302
        assert Check.objects.count() == 1

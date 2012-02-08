from unittest import TestCase

from dreamstack import base


class SofwareTestCase(TestCase):
    """
    """
    def test_scheme(self):
        sw = base.Software()
        self.assertEqual(sw.scheme, "type")

    def test_git_project(self):
        uri = "git://git@github.com:dreamhost/dreamstack-deploy.git"
        sw = base.Software(uri=uri)
        self.assertEqual(sw.git_project, "dreamstack-deploy")

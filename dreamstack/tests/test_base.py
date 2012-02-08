from unittest import TestCase

from dreamstack import base


class SoftwareTestCase(TestCase):
    """
    """
    def test_scheme(self):
        sw = base.Software()
        self.assertEqual(sw.scheme, "type")

    def test_path(self):
        sw = base.Software()
        self.assertEqual(sw.scheme, "type")


class GitSoftwareTestCase(SoftwareTestCase):

    def test_project(self):
        uri = "git://git@host.com:team/cool-project.git"
        git = base.GitSoftware(uri=uri)
        self.assertEqual(git.project, "cool-project")

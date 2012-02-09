from unittest import TestCase

from dreamstack import base


class SoftwareTestCase(TestCase):
    """
    """
    def setUp(self):
        uri = ("http://user:pass@host:port/path/to/some.thing"
               ";x;y;z?query=hey!#frag")
        self.software = base.Software(uri=uri)

    def test_parsed_uri(self):
        self.assertEqual(self.software.parsed_uri.scheme, "http")
        self.assertEqual(
            self.software.parsed_uri.netloc, "user:pass@host:port")
        self.assertEqual(self.software.parsed_uri.path, "/path/to/some.thing")
        self.assertEqual(self.software.parsed_uri.params, "x;y;z")
        self.assertEqual(self.software.parsed_uri.query, "query=hey!")
        self.assertEqual(self.software.parsed_uri.fragment, "frag")

    def test_scheme(self):
        self.assertEqual(self.software.scheme, "http")

    def test_path(self):
        self.assertEqual(self.software.path, "/path/to/some.thing")

    def test_query(self):
        self.assertEqual(self.software.query["query"], ["hey!"])

    def test_install(self):
        self.assertRaises(NotImplementedError, self.software.install)


class GitSoftwareTestCase(SoftwareTestCase):
    """
    """
    def setUp(self):
        self.software = base.GitSoftware(uri=self.get_uri())
        query = "tag=v1.0.2;other=thing;"
        commit_id = "532b6341b21e4dc2fffc5f4afbac465b23e2efb1"
        uri_extra = "%s?%s#%s" % (self.get_uri(), query, commit_id)
        self.software_extra = base.GitSoftware(uri=uri_extra)

    def get_uri(self):
        return "git://git@host.com:team/cool-project.git"

    def test_parsed_uri(self):
        self.assertEqual(self.software.parsed_uri.scheme, "git")
        self.assertEqual(self.software.parsed_uri.netloc, "git@host.com:team")
        self.assertEqual(self.software.parsed_uri.path, "/cool-project.git")
        self.assertEqual(self.software.parsed_uri.params, "")
        self.assertEqual(self.software.parsed_uri.query, "")
        self.assertEqual(self.software.parsed_uri.fragment, "")

    def test_scheme(self):
        self.assertEqual(self.software.scheme, "git")

    def test_path(self):
        self.assertEqual(self.software.path, "/cool-project.git")

    def test_project(self):
        self.assertEqual(self.software.project, "cool-project")

    def test_project_with_query(self):
        self.assertEqual(self.software_extra.project, "cool-project")

    def test_query(self):
        self.assertEqual(self.software_extra.query["other"], ["thing"])

    def test_tag(self):
        self.assertEqual(self.software_extra.tag, "v1.0.2")

    def test_commit_id(self):
        self.assertEqual(
            self.software_extra.commit_id,
            "532b6341b21e4dc2fffc5f4afbac465b23e2efb1")

    def test_install(self):
        pass


class GitPythonSoftwareTestCase(GitSoftwareTestCase):
    """
    """

    def get_uri(self):
        return "git+python://git@host.com:team/cool-project.git"

    def test_parsed_uri(self):
        self.assertEqual(self.software.parsed_uri.scheme, "git+python")
        self.assertEqual(self.software.parsed_uri.netloc, "git@host.com:team")
        self.assertEqual(self.software.parsed_uri.path, "/cool-project.git")
        self.assertEqual(self.software.parsed_uri.params, "")
        self.assertEqual(self.software.parsed_uri.query, "")
        self.assertEqual(self.software.parsed_uri.fragment, "")

    def test_scheme(self):
        self.assertEqual(self.software.scheme, "git+python")

    def test_install(self):
        pass


class SoftwareFactoryTestCase(TestCase):
    """
    """
    def test_git_software(self):
        software = base.softwareFactory("git://host:team/project.git")
        self.assertTrue(isinstance(software, base.GitSoftware))

    def test_read_only_git_software(self):
        software = base.softwareFactory("ro+git://host:team/project.git")
        self.assertTrue(isinstance(software, base.BaseGitSoftware))
        self.assertTrue(isinstance(software, base.ReadOnlyGitSoftware))

    def test_git_python_software(self):
        software = base.softwareFactory("git+python://host:team/project.git")
        self.assertTrue(isinstance(software, base.GitSoftware))
        self.assertTrue(isinstance(software, base.PythonSoftware))
        self.assertTrue(isinstance(software, base.GitPythonSoftware))

    def test_python(self):
        software = base.softwareFactory("python:///path/to/source/dir")
        self.assertTrue(isinstance(software, base.PythonSoftware))

    def test_apt_get(self):
        software = base.softwareFactory("apt-get:///path/to/deb")
        self.assertTrue(isinstance(software, base.AptGetSoftware))

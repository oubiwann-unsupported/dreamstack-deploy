from urllib2 import urlparse

from fabric.api import cd, local, run


class Software(object):
    """
    """
    uri = "type://path-or-uri"
    _type = ""
    _uri = ""
    _install_path = ""
    _execute = ""

    def __init__(self, uri=None, install_path="", method=""):
        if uri:
            self.uri = uri
        self.parsed_uri = urlparse.urlparse(self.uri)
        self._install_path = install_path
        if method == "local":
            self._execute = local
        elif method == "remote":
            self._execute = run

    @property
    def scheme(self):
        return self.parsed_uri.scheme

    @property
    def git_project(self):
        project = self.parsed_uri.path
        if project.startswith("/") and project.endswith(".git"):
            project = project[1:-4]
        return project

    def _install_git(self):
        with cd(self.install_path):
            self._execute("git clone %s" % self._uri)

    def _install_python(self):
        pass

    def _install_git_python(self):
        pass

    def install(self):
        if self.scheme == "git":
            self._install_git()
        elif self.scheme == "python":
            self._install_python()
        elif self.scheme == "git+python":
            self._install_git_python()

    def git_pull(self):
        pass

    def git_push(self):
        pass


class SoftwareCollection(object):
    """
    """
    def __init__(self, uris=None, install_path="", method=""):
        if not uris:
            uris = []
        self.uris = uris
        self.install_path = install_path
        self.method = method

    def append(self, *args, **kwargs):
        self.uris.append(*args, **kwargs)

    def install(self):
        for uri in self.uris:
            software = Software(uri, self.install_path, self.method)
            software.install()

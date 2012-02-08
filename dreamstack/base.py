from urllib2 import urlparse

from fabric.api import cd, local, run


class Software(object):
    """
    """
    uri = "type://path-or-uri"
    install_path = ""
    _type = ""
    _uri = ""
    _execute = ""

    def __init__(self, uri=None, install_path="", method=""):
        if uri:
            self.uri = uri
        self.parsed_uri = urlparse.urlparse(self.uri)
        self.install_path = install_path
        if method == "local":
            self._execute = local
        elif method == "remote":
            self._execute = run

    @property
    def scheme(self):
        return self.parsed_uri.scheme

    @property
    def path(self):
        return self.parsed_uri.path

    def install(self):
        """
        Subclasses need to implement this method.
        """
        raise NotImplementedError(self.instal.__doc__)


class AptGetSoftware(Software):
    """
    """


class PythonSoftware(Software):
    """
    """


class GitSoftware(Software):
    """
    This class consolidates methods and data particular to git repos.
    """
    @property
    def project(self):
        project = self.parsed_uri.path
        if project.startswith("/") and project.endswith(".git"):
            project = project[1:-4]
        return project

    def pull(self):
        pass

    def push(self):
        pass

    def install(self):
        with cd(self.install_path):
            self._execute("git clone %s" % self._uri)
        


class GitPythonSoftware(PythonSoftware, GitSoftware):
    """
    """


def softwareFactory(uri, *args, **kwargs):
    """
    """
    if uri.startswith("git+python://"):
        return GitPythonSoftware(uri, *args, **kwargs)
    elif uri.startswith("git://"):
        return GitSoftware(uri, *args, **kwargs)


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
            software = softwareFactory(uri, self.install_path, self.method)
            software.install()

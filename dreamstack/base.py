import urllib2 import urlparse


class Software(object):
    """
    """
    uri = "type://path-or-uri"
    _type = ""
    _uri = ""

    def __init__(self, uri=None):
        if uri:
            self.uri = uri
        self._uri = self.uri.split("://")[1]

    @property
    def type(self):
        if not self._type:
            self._type = urlparse.urlparse(self.uri)[0]
        return self._type

    def _install_git(self):
        pass

    def _install_python(self):
        pass

    def _install_git_python(self):
        pass

    def install(self):
        if self.type == "git":
            self._install_git()
        elif self.type == "python":
            self._install_python()
        elif self.type == "git+python":
            self._install_git_python()


class SoftwareCollection(object):
    """
    """
    def __init__(self, uris=None)
        if not uris:
            uris = []
        self.uris = uris

    def append(self, *args, **kwargs):
        self.uris.append(*args, **kwargs)

    def install(self):
        for uri in self.uris:
            software = Software(uri)
            software.install()

import os
from urllib2 import urlparse

from fabric.api import cd, local, run


dreamstack_schemes = ["git", "ro+git", "python", "git+python", "apt-get"]
urlparse.uses_relative.extend(dreamstack_schemes)
urlparse.uses_netloc.extend(dreamstack_schemes)
urlparse.non_hierarchical.extend(dreamstack_schemes)
urlparse.uses_params.extend(dreamstack_schemes)
urlparse.uses_query.extend(dreamstack_schemes)
urlparse.uses_fragment.extend(dreamstack_schemes)


class BaseSoftware(object):
    """
    """
    def __init__(self, uri="git://uri"):
        self.uri = uri
        self.parsed_uri = urlparse.urlparse(self.uri, scheme="http")

    @property
    def scheme(self):
        return self.parsed_uri.scheme

    @property
    def path(self):
        return self.parsed_uri.path

    @property
    def query(self):
        return urlparse.parse_qs(self.parsed_uri.query)


class ReadOnlySoftware(BaseSoftware):
    """
    """


class Software(BaseSoftware):
    """
    """
    _execute = ""

    def __init__(self, uri="git://uri", upstream="git://uri",
                 install_path="", method="local"):
        super(Software, self).__init__(uri=uri)
        self.upstream = softwareFactory("ro+%s" % upstream)
        self.install_path = install_path
        if method == "local":
            self._execute = local
        elif method == "remote":
            self._execute = run

    def install(self):
        """
        Subclasses need to implement this method.
        """
        raise NotImplementedError(self.install.__doc__)


class AptGetSoftware(Software):
    """
    """


class PythonSoftware(Software):
    """
    """


class BaseGitSoftware(BaseSoftware):
    """
    This class consolidates methods and data particular to git repos.
    """
    @property
    def project(self):
        project = self.parsed_uri.path
        if project.startswith("/") and project.endswith(".git"):
            project = project[1:-4]
        return project

    @property
    def tag(self):
        return self.query.get("tag")[0]

    @property
    def commit_id(self):
        return self.parsed_uri.fragment

    @property
    def project_dir(self):
        return os.path.join(self.install_path, self.project)

    def pull(self):
        with cd(self.project_dir):
            self._execute("git pull origin master")

    def checkout_tag(self):
        with cd(self.project_dir):
            self._execute("git checkout tags/%s" % self.tag)


class ReadOnlyGitSoftware(BaseGitSoftware):
    """
    """


class GitSoftware(BaseGitSoftware, Software):
    """
    """
    def push(self):
        with cd(self.project_dir):
            self._execute("git push origin master")

    def install(self):
        with cd(self.install_path):
            self._execute("git clone '%s'" % self.uri)


class GitPythonSoftware(PythonSoftware, GitSoftware):
    """
    Same as the GitSoftware class, except that this one also intsalls the
    Python project in the system library.
    """
    def install(self):
        GitSoftware.install(self)
        PythonSoftware.install(self)


def softwareFactory(uri, *args, **kwargs):
    """
    """
    if uri.startswith("git+python://"):
        uri = uri.split("git+python://")[1]
        return GitPythonSoftware(uri, *args, **kwargs)
    elif uri.startswith("git://"):
        uri = uri.split("git://")[1]
        return GitSoftware(uri, *args, **kwargs)
    elif uri.startswith("ro+git://"):
        uri = uri.split("ro+git://")[1]
        return ReadOnlyGitSoftware(uri, *args, **kwargs)
    elif uri.startswith("python://"):
        uri = uri.split("python://")[1]
        return PythonSoftware(uri, *args, **kwargs)
    elif uri.startswith("apt-get://"):
        uri = uri.split("apt-get://")[1]
        return AptGetSoftware(uri, *args, **kwargs)
    else:
        raise ValueError("Unknown software type for uri '%s'" % uri)


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
            software = softwareFactory(
                uri=uri, upstream=None, install_path=self.install_path,
                method=self.method)
            software.install()

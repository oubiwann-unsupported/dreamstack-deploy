from dreamstack import base


__all__ = ["NovaPersona", "QuantumPersona", "GlancePersona", "SwiftPersona",
           "KeystonePersona", "MySQLPersona",
          ]


class Persona(object):
    """
    A base class for a collection of software dependencies
    """
    def __init__(self, install_path="./", method=""):
        self.install_path = install_path
        self.method = method
        self._main_package = base.softwareFactory(
            self.main_package_uri, install_path, method)
        self._parent = base.softwareFactory(
            self.parent_uri, install_path, method)
        self._deps = base.SoftwareCollection(
            self.dependency_uris, install_path, method)

    def install(self):
        self._deps.install()
        self._main_package.install()
        self._parent.git_pull()
        self._main_package.git_push()


class NovaPersona(Persona):
    """
    """
    main_package_uri = "git://git@github.com:dreamhost/nova.git"
    parent_uri = "git://git@github.com:openstack/nova.git"
    dependency_uris = []


class QuantumPersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class GlancePersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class SwiftPersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class KeystonePersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class HorizonPersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class MySQLPersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class EC2GateWayPersona(Persona):
    """
    """
    main_package_uri = "git://"
    dependency_uris = []


class RADOSGatewayPersona(Persona):
    """
    """
    main_package_uri = ""
    dependency_uris = []


openstack = [
    NovaPersona, QuantumPersona, GlancePersona, SwiftPersona,
    KeystonePersona]
all = openstack + [
    MySQLPersona]

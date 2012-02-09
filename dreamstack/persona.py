from dreamstack import base


__all__ = ["NovaPersona", "QuantumPersona", "GlancePersona", "SwiftPersona",
           "KeystonePersona", "MySQLPersona",
          ]


class Persona(object):
    """
    A base class for a collection of software dependencies
    """
    main_package = "git://uri"
    upstream_package = "git://uri"
    dependencies = ["git://uri", "git://uri"]

    def __init__(self, install_path="./", method=""):
        self.install_path = install_path
        self.method = method
        self._main_package = base.softwareFactory(
            self.main_package, self.upstream_package, install_path, method)
        self._deps = base.SoftwareCollection(
            self.dependencies, install_path, method)

    def install(self):
        self._deps.install()
        self._main_package.install()
        self._main_package.push()


class NovaPersona(Persona):
    """
    """
    #main_package = "git://git@github.com:dreamhost/nova.git"
    #upstream_package = "git://git@github.com:openstack/nova.git"
    main_package = "git://git@github.com:dreamhost/dreamstack-deploy.git"
    upstream_package = "git://git@github.com:oubiwann/dreamstack-deploy.git"
    dependencies = []


class QuantumPersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class GlancePersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class SwiftPersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class KeystonePersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class HorizonPersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class MySQLPersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class EC2GateWayPersona(Persona):
    """
    """
    main_package = "git://"
    dependencies = []


class RADOSGatewayPersona(Persona):
    """
    """
    main_package = ""
    dependencies = []


openstack = [
    NovaPersona, QuantumPersona, GlancePersona, SwiftPersona,
    KeystonePersona]
all = openstack + [
    MySQLPersona]

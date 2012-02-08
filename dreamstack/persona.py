from dreamstack import base


__all__ = ["NovaPersona", "QuantumPersona", "GlancePersona", "SwiftPersona",
           "KeystonePersona", "MySQLPersona",
          ]


class Persona(object):
    """
    A base class for a collection of software dependencies
    """
    def __init__(self):
        self._main_package = base.Software(self.main_package_uri)
        self._deps = base.SoftwareCollection(self.dependency_uris)

    def install(self):
        self._deps.install()
        self._main_package.install()


class NovaPersona(Persona):
    """
    """
    main_package_uri = "git://git@github.com:dreamhost/nova.git"
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


all = [NovaPersona, QuantumPersona, GlancePersona, SwiftPersona,
       KeystonePersona, MySQLPersona,
      ]

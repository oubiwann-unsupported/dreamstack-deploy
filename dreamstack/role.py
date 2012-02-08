from dreamstack import persona


class Organizer(object):
    """
    A configuration base class to be used for organizing different deployment
    environments and system roles.
    """


# set up the SF development environment
sf = Organizer()
sf.bromine = Organizer()
sf.bromine.host = "192.168.221.111"
sf.bromine.personas = [
    persona.NovaPersona,
    ]
sf.chlorine = Organizer()
sf.chlorine.host = "192.168.221.113"
sf.chlorine.personas = [
    persona.MySQLPersona,
    persona.KeystonePersona,
    persona.GlancePersona,
    persona.SwiftPersona,
    ]


# set up the Atlanta development environment
atl = Organizer()
atl.somename1 = Organizer()
atl.somename2 = Organizer()


# set up a localhost development environment
localhost = Organizer()
localhost.local = Organizer()
localhost.local.host = "127.0.0.1"
localhost.personas = persona.all

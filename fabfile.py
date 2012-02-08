from fabric.api import env, local, run

from dreamstack import persona, target


env.hosts = target.servers


# XXX the meat of these functions may want to go into a dreamstack.script
# XXX module so that we can reuse checks for various deploy strategies.
def build_local_checkouts():
    # XXX once we've got a clean install running, we can test with an install
    # XXX that already exists.
    #base_dir = "~/lab/OpenStack")
    base_dir = "~/lab/OpenStack-2"
    local("mkdir -p %s" % base_dir)
    for klass in persona.openstack:
        component = klass(install_path=base_dir, method="local")
        print component
        print component.__dict__
        component.install()

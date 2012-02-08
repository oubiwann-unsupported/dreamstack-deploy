from fabric.api import env, run

from dreamstack import persona, target


env.hosts = target.servers


def build_local_checkouts():
    # XXX once we've got a clean install running, we can test with an install
    # XXX that already exists.
    #base_dir = "~/lab/OpenStack")
    base_dir = "~/lab/OpenStack-2")
    local("mkdir -p %s" % base_dir)
    for klass in persona.openstack:
        component = klass(install_path=base_dir, method="local")
        component.install()

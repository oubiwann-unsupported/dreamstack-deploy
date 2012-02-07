from fabric.api import local


def deploy():
    local("ls -al")

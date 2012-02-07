from fabric.api import env, run

from dreamstack import target


env.hosts = target.servers


def check():
    run("cat /tmp/doesnt/exist")

def deploy():
    #check()
    run("ls -al")

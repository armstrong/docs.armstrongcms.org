from fabric.api import *
fabric_local = local


def local(*cmds):
    for cmd in cmds:
        fabric_local(cmd, capture=False)


@task
def build():
    """Build documentation"""
    local("make clean dirhtml")


@task
def deploy():
    """Take built documentation and deploy it to GitHub"""
    local("git checkout gh-pages",
          "cp -R build/dirhtml/* .",
          "git add .",
          "git commit -m 'update to latest version of docs'",
          "git push armstrong gh-pages")
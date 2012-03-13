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
          "git push armstrong gh-pages",
          "git checkout master")


@task
def update_all():
    """Grab the latest code for all of the components"""
    local("for i in $(ls -1 vendor/); do cd vendor/$i && git pull origin master; cd ../.. ; done")


@task
def serve(port=8000):
    """Simple HTTP server for the docs"""
    import os
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    import SocketServer

    os.chdir("./build/dirhtml")
    httpd = SocketServer.TCPServer(("", port), SimpleHTTPRequestHandler)

    try:
        print "Serving documentation on %d" % port
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

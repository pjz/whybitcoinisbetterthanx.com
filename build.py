
import os.path
import contextlib
from fabricate import run, shell, autoclean, main

UIKIT='Flat-UI-master'
BUILDDIR='output'
S3_BUCKET='s3://whybitcoinisbetterthanx.com'

# random utility
@contextlib.contextmanager  
def chdir(dirname=None):  
    curdir = os.getcwd()  
    try:  
        if dirname is not None:  
            os.chdir(dirname)  
        yield  
    finally:  
        os.chdir(curdir)

# actual build process
def build():
    run('mkdir', BUILDDIR)
    for d in [ 'css', 'fonts', 'images', 'js', 'sass' ]:
        run('cp', '-r', os.path.join(UIKIT, d), BUILDDIR)
    run('cp', '-r', 'www/*', BUILDDIR, shell=True)

def publish():
    build()
    shell('s3cmd', 'sync', BUILDDIR + '/', S3_BUCKET)

def clean():
    autoclean()
    shell('rm','-rf', BUILDDIR)

def show_targets():
    print("""Valid targets:

        show_targets - this
        build - build into """ + BUILDDIR + """
        publish - publish up to S3, building if necessary
        clean - clean out """ + BUILDDIR + """
""")

main()


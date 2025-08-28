#!/usr/bin/python3

import os
import setuptools
import subprocess
import setuptools.command.sdist
import setuptools.command.install
from distutils import log

with open("README.md", "r") as fh:
    long_description = fh.read()


manpage = 'rsnappush.1'

def run(cmd):
    log.info("calling " + ' '.join(cmd))
    subprocess.run(cmd, check=True)

    
class my_sdist(setuptools.command.sdist.sdist):
    def run(self):
        cmd = ["ronn", "--roff", "README.md"]
        run(cmd)
        
        cmd = ["mv", "README.1", manpage]
        run(cmd)
        
        super().run()
        

class my_install(setuptools.command.install.install):
    def run(self):
        os.umask(0o002)
        run(['chmod', '-R', 'a+rX', 'rsnappush.egg-info'])
        
        stat = os.stat(manpage)
        os.chmod(manpage, stat.st_mode | 0o444)
        super().run()

        
setuptools.setup(name='rsnappush',
                 version = '1.1',
                 packages = setuptools.find_packages(),
                 url = "https://github.com/ftobin/rsnappush",
                 license = "MPL-2.0",
                 author = "Frank Tobin",
                 author_email = "ftobin@neverending.org",
                 description = "rsync-based pushed incremental snapshot",
                 long_description = long_description,
                 platforms = "POSIX",
                 scripts=["rsnappush"],
                 data_files=[('share/man/man1/', [manpage])],
                 cmdclass = {'sdist': my_sdist,
                             'install': my_install,
                 },
)

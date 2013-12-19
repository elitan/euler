from distutils.core import setup, Extension

module1 = Extension('pariparse',
                    include_dirs = ['/usr/include', '/usr/local/include'],
                    libraries = ['pari'],
                    library_dirs = ['/usr/lib', '/usr/local/lib'],
                    sources = ['pariparse.c'])

setup (name = 'pariparse',
       version = '0.01a',
       description = 'A super tiny python-pari interface',
       ext_modules = [module1])
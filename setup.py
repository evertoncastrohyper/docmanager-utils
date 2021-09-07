from setuptools import setup
setup(
    name='docmanagerutils',
    version='0.0.1',
    description='Doc Manager Utils',
    url='https://github.com/evertoncastrohyper/docmanager-utils',
    author='Everton Castro',
    author_email='everton.castro@hyperativa.com.br',
    license='MIT',
    packages=['docmanagerutils'],
    zip_safe=False,
    install_requires=[
       "google-auth",
       "google-cloud-core",
   ]
)
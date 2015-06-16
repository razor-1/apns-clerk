import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='apns-clerk',
    version='0.2.0',
    author='Aleksi Hoffman',
    author_email='aleksi@lekksi.com',
    url='https://bitbucket.org/aleksihoffman/apns-clerk',
    description='Python client for Apple Push Notification service (APNs)',
    long_description=read('README.rst'),
    packages=['apns_clerk', 'apns_clerk.backends'],
    license="Apache 2.0",
    keywords='apns push notification apple messaging iOS',
    install_requires=['pyOpenSSL', 'six'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)

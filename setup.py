from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

from os import path


# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
dependency_links = []

# Inject requirements from requirements.txt into setup.py
requirements_file = parse_requirements(path.join('requirements', 'requirements.txt'), session=PipSession())
for req in requirements_file:
    install_requires.append(str(req.req))
    if req.link:
        dependency_links.append(str(req.link))

# Inject test requirements from requirements_test.txt into setup.py
requirements_test_file = parse_requirements(path.join('requirements', 'requirements_test.txt'), session=PipSession())
for req in requirements_test_file:
    tests_require.append(str(req.req))
    if req.link:
        dependency_links.append(str(req.link))


# Became django-statsd-unleashed because django-statsd and django-statsd-mozilla are taken on Pypi. ;)
setup(
    name='django-statsd-unleashed',
    version='1.0.1',
    url='https://github.com/vikingco/django-statsd',
    license='BSD',
    description='Django interface with statsd',
    long_description=open('README.rst').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    maintainer='Unleashed NV',
    maintainer_email='operations@unleashed.be',
    packages=find_packages('.'),
    entry_points={
        'nose.plugins.0.10': [
            'django_statsd = django_statsd:NoseStatsd'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    test_suite = 'nose.collector',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)

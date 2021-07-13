#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "bump2version==0.5.11",
    "wheel==0.33.6",
    "watchdog==0.9.0",
    "flake8==3.9.1",
    "tox==3.14.0",
    "coverage==4.5.4",
    "Sphinx==1.8.5",
    "twine==1.14.0",
    "jsonpath_ng==1.5.2"
]

setup_requirements = []

test_requirements = []

setup(
    author="Matthew Bailey",
    author_email='Matthew.F.Bailey@outlook.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Package to facilitate rescheming data to json",
    entry_points={
        'console_scripts': [
            'json_reschemer=json_reschemer.cli:run',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='json_reschemer',
    name='json_reschemer',
    packages=find_packages(include=['json_reschemer', 'json_reschemer.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/matthew-f-bailey/json_reschemer',
    version='0.1.0',
    zip_safe=False,
)

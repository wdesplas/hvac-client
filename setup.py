#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='hvac-client-status',
    version='0.0.1',
    python_requires='>=3.5',
    packages=find_packages(exclude=['tests']),
    install_requires=['flask','hvac'],
    test_suite="tests",


    # Metadata
    author="Willy DESPLAS",
    author_email="willy@desplas.com",
    license="MIT",
    description="client for testing availability, backup and restoration of the Vault services",
    long_description=open('README.md').read(),
    url="https://github.com/wdesplas/hvac",
    keywords=["cloudfoundry", "vault", "havc", "flask"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Frameworks
        'Framework :: Flask',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: AGPLv3 License',

        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']}

)

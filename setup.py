#!/usr/bin/env python

from setuptools import setup
import versioneer

setup(name='s3fs',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
      ],
      description='Convenient Filesystem interface over S3',
      url='http://github.com/dask/s3fs/',
      maintainer='Martin Durant',
      maintainer_email='mdurant@continuum.io',
      license='BSD',
      keywords='s3, boto',
      packages=['s3fs'],
      python_requires='>= 2.7, != 3.0.*, != 3.1.*, != 3.2.*, != 3.3.*',
      install_requires=[open('requirements.txt').read().strip().split('\n')],
      zip_safe=False)

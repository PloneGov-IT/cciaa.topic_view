# -*- coding: utf-8 -*-
"""
This module contains the tool of cciaa.topic_view
"""
import os
from setuptools import setup, find_packages

version = '1.1.2.dev0'

tests_require=['zope.testing']

setup(name='cciaa.topic_view',
      version=version,
      description="Additional view for Collection in Plone, with a common C2P/C3P CCIAA layout",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='plone plonegov collection view home-page',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.net',
      url='https://code.redturtle.it/svn/camera_di_commercio_fe/C3P/cciaa.topic_view/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cciaa', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'cciaa.topic_view.tests.test_docs.test_suite',
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

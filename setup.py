from setuptools import setup, find_packages
import os

version = '1.1.dev0'

setup(name='collective.js.twittertext',
      version=version,
      description="Add twitter-text.js library to Plone's resource registry",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/collective/collective.js.twittertext',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

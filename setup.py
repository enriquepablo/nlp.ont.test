from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='nlp.ont.test',
      version=version,
      description="test ontology",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='nl ontology',
      author='Enrique P\xc3\xa9rez Arnaud',
      author_email='enriquepablo@gmail.com',
      url='http://enriquepablo.github.com/nlproject/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nlp', 'nlp.ont'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

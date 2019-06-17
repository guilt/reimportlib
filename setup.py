"""
reimportlib: refactored imports
"""
from setuptools import setup, find_packages

VERSION = '1.0'

setup(name='reimportlib',
      version=VERSION,
      description="reimportlib: refactored imports",
      long_description="A library to help with maintaining compatibility with refactored code.",
      classifiers=['Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='importlib refactor module rename move serialize',
      author='Karthik Kumar Viswanathan',
      author_email='karthikkumar@gmail.com',
      url='http://karthikkumar.org',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'examples.*', 'tests']),
      include_package_data=False,
      zip_safe=True,
      install_requires=[],
     )

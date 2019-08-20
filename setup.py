from setuptools import setup

setup(name='a2dr',
      version='0.1',
      description='A package for generalized consensus optimization using the alternating direction method of multipliers (ADMM).',
      url='http://github.com/anqif/a2dr',
      author='Anqi Fu, Junzi Zhang, Stephen Boyd',
      author_email='anqif@stanford.edu',
      license='Apache License, Version 2.0',
      packages=['a2dr'],
      install_requres=['collections',
		       'matplotlib',
		       'multiprocess',
		       'tabulate',
		       'time',
		       'cvxpy >= 1.0',
		       'numpy >= 1.14',
               'scikit-sparse >= 0.1'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])

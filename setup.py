"""Define the redis-naming-py package configration."""

from distutils.core import setup

setup(name='redisnaming',
      version='1.0',
      description='Provide the function to build key and value on the ' +
      'naming convention that proposed by the Redis documentation.',
      author='Sho Minagawa',
      author_email='msh5.global@gmail.com',
      url='http://github.com/msh5/redis-naming-py',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Database',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='redis',
      packages=['redisnaming'],
      )

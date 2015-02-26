from setuptools import find_packages
from setuptools import setup


setup(name='falconpb',
      version='1.0.0',
      description='Protocol Buffers based resource for Falcon',
      keywords='falcon protocol buffers protobuf',
      classifiers=[
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='http://github.com/5amfung/falconpb',
      author='Sam Fung',
      author_email='sam.fung@gmail.com',
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'falcon>=0.2',
          'protobuf-to-dict>=0.1.0'
      ])

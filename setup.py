from setuptools import setup, find_packages


setup(
    name='tvdb_monitor',
    version='1.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=['logbook', 'requests', 'beautifulsoup4', 'ujson', 'tvdb_api', 'guessit'],
    entry_points={
      'console_scripts': [
          'tvdb_monitor = monitor:main',
      ]
    }
)

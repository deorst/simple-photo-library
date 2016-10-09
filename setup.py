from setuptools import setup

setup(name='simpholib',
      version='0.1',
      description='Simple photo library',
      url='https://github.com/dstdnk/simple-photo-library',
      author='Dmitry Stadnik',
      author_email='dmitry.stadnik.mail@gmail.com',
      license='MIT',
      packages=['simpholib'],
      zip_safe=False,
      entry_points={
          'console_scripts': ['simpho=simpholib.command_line:main'],
      }
    )
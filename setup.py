from setuptools import setup, find_packages


setup(name='qmongohelper',
    version='0.1',
    description='a simple way to use mongo db, let db like dict',
    url='https://github.com/Qingluan/QmongoHelper.git',
    author='Qing luan',
    author_email='darkhackdevil@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
          'motor',
          'tornado',
      ],

)

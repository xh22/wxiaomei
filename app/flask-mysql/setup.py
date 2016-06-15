"""
Flask-mysql
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-mysql',
    version='1.0',
    url='http://example.com/flask-mysql/',
    license='BSD',
    author='Your Name',
    author_email='your-email@example.com',
    description='Very short description',
    long_description=__doc__,
    py_modules=['flask_mysql'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_mysql'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

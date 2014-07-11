from setuptools import setup, find_packages

setup(
    name = "django-shorturls",
    version = "1.0",
    url = 'http://github.com/jacobian/django-shorturls',
    license = 'BSD',
    description = "A short URL handler for Django apps.",
    author = 'Jacob Kaplan-Moss',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
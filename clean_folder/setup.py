from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    # description='Very useful code',
    # url='http://github.com/dummy_user/useful',
    author='Olexander Zh.',
    # author_email='flyingcircus@example.com',
    # license='MIT',
    packages=find_namespace_packages(),
    # install_requires=['markdown'],
    entry_points={'console_scripts': ['clean=clean_folder.main:start']}
)
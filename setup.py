from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return dict(package=stubs)


setup(
    name='MaterialX-stubs',
    maintainer="MaterialX Developers",
    maintainer_email="example@python.org",
    description="PEP 561 type stubs for MaterialX",
    version='1.0',
    packages=['MaterialX-stubs'],
    # PEP 561 requires these
    install_requires=['MaterialX'],
    package_data=find_stubs('MaterialX-stubs'),
)
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in local1/__init__.py
from local1 import __version__ as version

setup(
	name="local1",
	version=version,
	description="About Local",
	author="Other",
	author_email="aaa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

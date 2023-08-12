from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in inventory/__init__.py
from inventory import __version__ as version

setup(
	name="inventory",
	version=version,
	description="Creating the Inventory Management",
	author="Jagadeesan",
	author_email="jagadeesan1104@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

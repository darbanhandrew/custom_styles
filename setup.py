from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_styles/__init__.py
from custom_styles import __version__ as version

setup(
	name="custom_styles",
	version=version,
	description="An app for adding custom styles to erpnext",
	author="Mohammad Darban Baran",
	author_email="darbanhandrew@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)


from setuptools import setup, find_packages

setup(name="da_plugin",
	version="0.1",
	description="da-plugin package",
	url="https://github.com/fumiya-kubota/da-plugin",
	packages=find_packages(),
    include_package_data=True,
    package_dir={'da_plugin': 'da_plugin'},
    package_data={'da_plugin': ['js/*.js', 'js/**/*.js']}
)

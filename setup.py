
from setuptools import setup, find_packages

setup(name="da_plugin",
	version="0.1",
	description="da-plugin package",
	url="https://github.com/fumiya-kubota/da-plugin",
	packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('da_plugin', ['js/index.js', 'js/components/PluginComponent.js']),
    ]
)

"""
Resume site python package configuration.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sqlite_rsm',
    version='0.1.0',
    packages=['sqlite_rsm'],
    author="Thomas Dokas",
    author_email="dokastho@umich.edu",
    url="https://github.com/dokastho/sqlite-rsm",
    description="An RSM container for hosting an SQLite instance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sqlite_rsm-viewer = sqlite_rsm.viewer.__main__:main',
            'sqlite_rsm-node = sqlite_rsm.node.__main__:main',
            'sqlite_rsm = sqlite_rsm.bootstrap:main'
        ]
    },
)

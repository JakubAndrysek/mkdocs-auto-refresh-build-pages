from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


def import_requirements():
    """Imports requirements from requirements.txt file."""
    with open("requirements.txt") as f:
        return f.read().splitlines()


def import_dev_requirements():
    """Imports requirements from devdeps.txt file."""
    with open("devdeps.txt") as f:
        return f.read().splitlines()


# https://pypi.org/project/mkdocs-auto-refresh-build-pages
setup(
    name="mkdocs-auto-refresh-build-pages",
    version="1.0.0",
    description="MkDocs plugin that automatically refreshes the build pages when the page has been rebuilt.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="mkdocs plugin, mkdocs, auto refresh, auto refresh build pages",
    url="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages",
    author="Jakub Andrýsek",
    author_email="email@kubaandrysek.cz",
    license="MIT",
    python_requires=">=3.7",
    install_requires=import_requirements(),
    extras_require={
        "dev": import_dev_requirements(),
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "mkdocs.plugins": [
            "auto-refresh-build-pages = auto_refresh_build_pages.plugin:AutoRefreshBuildPages",
        ]
    },
)

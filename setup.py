from setuptools import setup, find_packages

setup(
    name="entity-linking",
    version="0.1.0",
    author="Will Thompson",
    author_email="will.k.t@gmail.com",
    packages=find_packages(include=["elinker", "elinker.*"]),
    package_data={"elinker": ["data/*"]},
    include_package_data=True,
    install_requires=[
        "spacy",
        "pandas",
        "seaborn",
        "transformers",
        "datasets",
        "typer",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "elinker=elinker.cli:app",
        ],
    },    extras_require={
        "interactive": ["jupyterlab"],
        "dev": ["black", "pyment", "twine", "tox", "bumpversion", "flake8"],
        "test": ["pytest"],
    },
    python_requires=">=3.9.0",
)

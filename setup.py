from setuptools import setup

setup(
    name="stackeddiff",
    version="0.1",
    description="Stacked diffs in python",
    url="",
    author="",
    author_email="",
    license="MIT",
    packages=["stack"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["stack=stack.cli:main"],
    },
)

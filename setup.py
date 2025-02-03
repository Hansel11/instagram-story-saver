from setuptools import *

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = list()
with open("requirements.txt", "r") as file:
    requirements = [r for r in file.readlines() if len(r) > 0]


setup (
    name="instastorysaver",
    author="Hansel11",
    version="0.1.2",
    packages=find_packages(),
        entry_points={
        "console_scripts": ["igsave=instastorysaver:main"],
    },
    description="Instagram Story Saver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hansel11/instagram-story-saver",
    include_package_data=True,
    install_requires=requirements,
)

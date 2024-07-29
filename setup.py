from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    mentioned in the given file.
    """
    requirements = []
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

    return requirements

__version__ = "0.0.4"
REPO_NAME = "Phishing_proejct_end_to_end"
PKG_NAME = "Phishingdetectiondomain"
AUTHOR_USER_NAME = "Deepak singh"
AUTHOR_EMAIL = "itsdeepaksingh00@gmail.com"

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PKG_NAME,  # Using the new package name
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements.txt"),  # Ensure this file contains your dependencies
    license_files=('LICENSE.txt',),  # Use license_files instead of license_file
)

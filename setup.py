import setuptools

__version__ = "0.0.0"

REPO_NAME = "IMD_WQP"
AUTHOR_USER_NAME = "Musician9dx"
SRC_REPO = "WQP"
AUTHOR_EMAIL = "vamsir863@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
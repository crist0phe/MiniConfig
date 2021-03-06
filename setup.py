import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()
long_description="Desc"

setuptools.setup(
    name="miniconfig",
    version="0.9",
    author="Christophe Godart",
    author_email="dev@armaghast.eu",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crist0phe/MiniConfig",
    packages=["miniconfig"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

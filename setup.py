import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywalrus",
    version="0.0.2",
    author="silverback",
    author_email="hello@clivern.com",
    description="A Python Package for Email Automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silverbackhq/pywalrus",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=["pytz"],
    license="MIT",
    platforms=['any'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
)

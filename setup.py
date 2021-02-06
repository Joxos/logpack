import setuptools

setuptools.setup(
    name="logpack",
    version="1.4",
    author="Joxos",
    author_email="xujunhao61@163.com",
    description="Log for Python!",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/Joxos/logpack",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
# Note:
# python setup.py sdist
# twine upload ./dist/*

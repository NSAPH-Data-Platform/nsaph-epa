from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()


setup(
    name='epa',
    version="0.0.1.1",
    url='https://gitlab-int.rc.fas.harvard.edu/rse/francesca_dominici/tools/epa',
    license='',
    author='Michael Bouzinier',
    author_email='mbouzinier@g.harvard.edu',
    description='EPA Data Pipelines',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    #py_modules = [''],
    package_dir={
        "epa": "./src/python/epa"
    },
    packages=["epa"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Harvard University :: Development",
        "Operating System :: OS Independent"],
    install_requires=[
        'fiona',
        'geopandas',
        'numpy',
        'pandas',
        'pygeos==0.10',
        'pyshp',
        'PyYAML',
        'requests',
        'PyYAML',
        'nsaph_utils >= 0.0.4.2',
        'nsaph>=0.0.2.0'
    ],
    package_data = {
        '': ["**/*.yaml"]
    }
)

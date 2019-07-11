from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lambdata-richmondtest',
    version='0.0.8',
    description='Helper functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['lambdata_richmondtest'],
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=0.24.2',
        'scipy>=1.3.0',
        'tabulate>=0.8.3',
        'seaborn>=0.8.3',
        'scikit-learn>=0.21.2'
    ]
)

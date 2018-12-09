from setuptools import setup, find_packages

# This file will install all the packages. To run this file do: 
# $ python setup/py develop

setup(
	name='data_analysis',
	version='0.0.1',
	url='www.github.com/GinaGrg1/data-analysis-using-python',
	license='BSD',
	author='Regina Gurung',
	packages=find_packages(),
	install_requires=['PyQt5', 'pandas', 'sqlalchemy', 'nltk', 'numpy', 'jupyter', 'python-twitter'],
	entry_points={},
	extras_require={'dev': ['flake8',]},
	)

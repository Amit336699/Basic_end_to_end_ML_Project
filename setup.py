from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the List of requirements
    '''

    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', "") for req in requirement]

    return requirement

setup(
    name='mlProject',
    version='0.0.1',
    author='amit',
    author_email='amitchamoli3699@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
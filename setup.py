from setuptools import find_packages,setup
from typing import List
Hy='-e .'

def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as fil_obj:
        requirement=fil_obj.readlines()
        requirement=[req.replace("\n","") for req in  requirement]

        if Hy in requirement:
            requirement.remove(Hy)
    return requirement


setup (
    name='dlprojects',
    version='0.0.1',
    author="prakash",
    author_email='athi4prakash@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')

)
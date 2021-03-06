# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = open('requirements.txt').read().split('\n')

setup(
    name='ocrd_kwalitee_dashboard_back_end',
    version='0.1.0',
    description='Back end for the OCR-D kwalitee dashboard webapp',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Konstantin Baierer',
    author_email='unixprog@gmail.com',
    url='https://github.com/OCR-D/kwalitee-dashboard-back-end',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=install_requires,
    package_data={
        '': ['*.json', '*.yml', '*.yaml', '*.list', '*.xml'],
    },
    entry_points={
        'console_scripts': [
            'ocrd-kwalitee=kwalitee.cli:cli',
        ]
    },
)

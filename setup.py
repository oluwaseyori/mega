from setuptools import setup, find_packages

setup(
    name='mega',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Seyori',
    description='Custom Mega.nz wrapper for large file transfers without bandwidth limits.',
    url='https://github.com/oluwaseyori/mega',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)

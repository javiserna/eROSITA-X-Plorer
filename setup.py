from setuptools import setup, find_packages

setup(
    name='erositaviz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'astropy',
        'astroquery',
        'numpy',
        'matplotlib',
    ],
    author='Javier Serna',
    author_email='jserna@astro.unam.mx',
    description='A package for eROSITA data visualization.',
    url='https://github.com/javiserna/erositaviz',
    license='MIT',
)


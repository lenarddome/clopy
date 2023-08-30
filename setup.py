from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="clobe", 
        version=VERSION,
        author="Lenard Dome",
        author_email="lenarddome@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['computational modelling', 'g-distance'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Linux :: Ubuntu",
            "Operating System :: Microsoft :: Windows",
        ]
)
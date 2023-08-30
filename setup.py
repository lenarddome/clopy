from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'Global Benchmark and Evaluation Tools for Formal Computational Models'
LONG_DESCRIPTION = ' Provides tools for the qualitative evaluation of formal computational models. Currently incorporates tools used in comparing model and human heterogeneity, see Dome and Wills (2023) <doi:10.31234/osf.io/ygmcj>.'

# Setting up
setup(
        name="clopy", 
        version=VERSION,
        author="Lenard Dome",
        author_email="lenarddome@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy'], # add any additional packages that 
        
        keywords=['computational modelling', 'g-distance', 'discretization', 'ordinal analysis'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Linux :: Ubuntu",
            "Operating System :: Microsoft :: Windows",
        ]
)
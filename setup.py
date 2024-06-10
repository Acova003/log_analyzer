from setuptools import setup, find_packages

setup(
    name='log_analyzer',
    version='0.1.0',
    author='Amee Covarrubias',  
    description='A command-line tool to analyze log files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Acova003/log_analyzer.git',  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
        'numpy',  
    ],
    entry_points={
        'console_scripts': [
            'log_analyze=log_analyzer.cli:analyze',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)



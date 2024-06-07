from setuptools import setup, find_packages

setup(
    name='log_analyzer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'log_analyze=log_analyzer.cli:analyze',
        ],
    },
)


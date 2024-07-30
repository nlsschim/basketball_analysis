from setuptools import setup, find_packages

setup(
    name='basketball_analysis',
    version='0.1',
    packages=find_packages('basketball_analysis'),
    package_dir={'': 'basketball_analysis'},
    install_requires=[
        'pandas',
        'numpy',
        'altair',
        'streamlit',
        'basketball_analysis',
    ],
    url="https://github.com/nlsschim/basketball_analysis"

)

from setuptools import setup

setup(
    name="random_walker",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        random_walker=main:cli
    '''
)
from setuptools import setup

setup(
    name='gctts',
    version='1.0',
    py_modules=['gctts'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        gctts=gctts:cli
    ''',
)
from setuptools import setup

setup(
    name='cdev',
    version='0.1',
    author='Dan Kilman',
    author_email='dankilman@gmail.com',
    packages=['cdev'],
    description='cloudify-dev CLI',
    zip_safe=False,
    install_requires=[
        'workflowcmd==0.1'
    ],
    entry_points={
        'console_scripts': [
            'cdev = cdev:main',
        ]
    },

)

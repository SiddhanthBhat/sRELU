from setuptools import setup, find_packages

setup(
    name='srelu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
    ],
    author='Siddhanth Bhat',
    author_email='siddhanthbhat@outlook.com',
    description='A library for the SReLU activation function.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SiddhanthBhat/sRELU',  # GitHub repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='anvil-new',
    version='1.0.1',
    author='intergalactyc',
    description='A Minecraft anvil file format parser, designed to work with minecraft versions 1.16+.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/intergalactyc/anvil-new',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'nbt',
        'frozendict',
    ],
    include_package_data=True
)

import setuptools

'''with open("README.md", "r") as fh:
    long_description = fh.read()'''
    
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="modbuscu",
    version="0.0.1",
    install_requires=requirements,
    author="Bartłomiej Hirsz",
    author_email="bartek.hirsz@gmail.com",
    description="Central Unit for controlling Modbus devices",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/MuminekM/ModbusCU",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
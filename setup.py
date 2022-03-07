from setuptools import setup

with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='python-test',
    version='0.1.0',
    url='https://github.com/belenalegre/-python-test.git',
    author='Belen Alegre',
    author_email='belen.alegre.za@gmail.com',
    description='Colektia ETL process test',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='3.8'
)
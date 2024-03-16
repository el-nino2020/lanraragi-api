from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()
    requirements = [r.strip() for r in requirements]

setup(
    name="lanraragi_api",
    version="0.0.1",
    description="a Python library for LANraragi API",
    packages=find_packages(),
    url="https://github.com/el-nino2020/lanraragi-api",
    author="El nino",
    author_email="el-nino202020@protonmail.com",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown'
)

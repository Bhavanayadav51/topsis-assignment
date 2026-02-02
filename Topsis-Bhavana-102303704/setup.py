from setuptools import setup, find_packages

setup(
    name="topsis_bhavana_102303704",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        'console_scripts': [
            'topsis=topsis_bhavana_102303704.topsis:topsis'
        ]
    },
    author="Bhavana Yadav",
    description="A Python package implementing TOPSIS method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT"
)

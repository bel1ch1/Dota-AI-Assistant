from setuptools import setup, find_packages

setup(
    name="dota-ai-assistant",
    version="0.1.0",
    description="AI Assistant for Dota 2",
    author="bel1ch1",
    author_email="andreyzv5555@gmail.com",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[
        "ruamel-yaml>=0.18.15,<0.19.0",
        "zenml[server]>=0.84.3,<0.85.0"
    ],
    python_requires=">=3.11,<3.13",
)

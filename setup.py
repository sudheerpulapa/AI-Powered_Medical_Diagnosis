from setuptools import setup, find_packages

# Read the content of your README file
from pathlib import Path
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text()

setup(
    name="Generative AI Project with LLMs: Medical Diagnosis",
    version="0.1.0",
    author="Sudheer Pulapa",
    author_email="sudheerpulapa@gmail.com",
    description="AI-Powered Medical Diagnosis",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[]
)

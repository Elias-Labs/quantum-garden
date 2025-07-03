#!/usr/bin/env python3
"""Setup script for Quantum Garden"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantum-garden",
    version="0.1.0",
    author="Mychal Simka",
    author_email="mychal@eliaslabs.com",
    description="AI Agent Orchestration Platform - Build your own AI workforce",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msimka/quantum-garden",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0",
        "pydantic>=2.0",
        "httpx>=0.24",
        "rich>=13.0",
        "python-dotenv>=1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "ruff>=0.1",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "quantum-garden=quantum_garden.cli:main",
            "qg=quantum_garden.cli:main",  # Short alias
        ],
    },
)
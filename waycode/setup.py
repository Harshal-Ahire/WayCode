from setuptools import setup, find_packages

# Load long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="waycode",
    version="1.0.0",
    author="Harshal Pramod Ahire",
    author_email="harshal.ahire@example.com",
    description="AI-Powered Code Refactoring Assistant with RAG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harshal-Ahire/WayCode",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    # Core dependencies for AI and vector storage
    install_requires=[
        "google-genai>=1.0.0",
        "python-dotenv>=1.0.0",
        "chromadb>=0.4.0",
        "numpy>=1.24.0",
        "click>=8.1.0",
    ],
    # CLI entry point
    entry_points={
        "console_scripts": [
            "waycode=waycode.cli:main",
        ],
    },
)

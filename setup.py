from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if any
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",  # Replace `main` if you use a different function to start
        ],
    },
)

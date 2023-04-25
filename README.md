# Inflam

![Continuous Integration build in GitHub Actions] (https://github.com/hj8367/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)
Inflam is a data management systen written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:
- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Procedures
The use of a virtual environment is recommended when using this code.
The following details some steps to take for set up:
- [Cloning the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- Create a virtual environment, e.g. using [venv](https://docs.python.org/3/library/venv.html)
- Activate the virtual environment. e.g. Using source venv/bin/activate
- Install the requirements for the project into the virtual environment. e.g. using pip install -r requirements.txt
This should result in a useable installation and environment.

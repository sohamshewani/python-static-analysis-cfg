# python-static-analysis-cfg

## Badges

[![GitHub license](https://img.shields.io/github/license/alibaba/python-static-analysis-cfg)](https://github.com/alibaba/python-static-analysis-cfg/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/v/tag/alibaba/python-static-analysis-cfg)](https://github.com/alibaba/python-static-analysis-cfg/releases)
[![Build Status](https://github.com/alibaba/python-static-analysis-cfg/workflows/CI/badge.svg)](https://github.com/alibaba/python-static-analysis-cfg/actions)
[![Coverage Status](https://coveralls.io/repos/github/alibaba/python-static-analysis-cfg/badge.svg?branch=main)](https://coveralls.io/github/alibaba/python-static-analysis-cfg?branch=main)

## Executive Overview & Problem Statement

`python-static-analysis-cfg` is an open-source project designed to provide robust static code analysis capabilities for Python projects. The primary goal is to enhance code quality and maintainability by identifying potential issues, such as security vulnerabilities, code smells, and complex or convoluted code patterns. This tool supports various Python environments and integrates seamlessly with existing development workflows.

The problem it addresses is the need for reliable, automated static code analysis in large-scale Python projects. Traditional static analysis tools often lack comprehensive coverage or are too complex to integrate into the development pipeline. `python-static-analysis-cfg` aims to bridge this gap by offering a lightweight, yet powerful, solution.

## ASCII Architecture / Flow Diagram

```ascidiagram
+---------------------------------------------------------+
|  User  +---------------------------------------+         |
|        |                                       |         |
|        |  +---------------------+              |         |
|        +--| CLI Interface      |              |         |
|          +---------------------+              |         |
|          |                                 |         |
|          v                                 |         |
|  +-----------------------------+   +------------------+  |
|  |                             |   |                  |  |
|  |   Configuration Management  |   |  Static Analysis  |  |
|  |                             |   |                  |  |
|  +-----------------------------+   +------------------+  |
|          |                                 |         |
|          v                                 |         |
|  +-----------------------------+   +------------------+  |
|  |                             |   |                  |  |
|  |   Code Parsing              |   |  Issue Detection  |  |
|  |                             |   |                  |  |
|  +-----------------------------+   +------------------+  |
|          |                                 |         |
|          v                                 |         |
|  +-----------------------------+   +------------------+  |
|  |                             |   |                  |  |
|  |   Reporting                 |   |  Integration     |  |
|  |                             |   |                  |  |
|  +-----------------------------+   +------------------+  |
|          |                                 |         |
|          v                                 |         |
+---------------------------------------------------------+
```

## Algorithmic & Design Decisions

### Concurrency Model

`python-static-analysis-cfg` is designed to handle large codebases efficiently using a multi-threaded approach. The tool utilizes Python's `concurrent.futures` module to manage tasks concurrently, ensuring that the analysis process does not become a bottleneck in the development cycle.

### Data Structures

- **AST Trees:** The tool uses Python's `ast` module to parse and represent the code in an Abstract Syntax Tree (AST). This allows for efficient traversal and analysis of the code structure.
- **Issue Storage:** Issues detected during the analysis are stored in a dictionary-like structure, facilitating quick access and reporting.
- **Configuration Management:** Configuration data is stored in a YAML file, allowing for flexible and extensible configuration options.

### Trade-offs

- **Performance vs. Flexibility:** While the tool is designed to be efficient, the flexibility in configuration comes at the cost of increased complexity in the setup and configuration process.
- **Complexity vs. Maintainability:** The multi-threaded architecture and modular design enhance maintainability but add to the complexity of the codebase.

## Installation, Build Instructions & CLI Command Recipes

### Prerequisites

- Python 3.8 or higher
- Poetry (optional, for project dependencies)

### Installation

You can install `python-static-analysis-cfg` from PyPI:

```sh
pip install python-static-analysis-cfg
```

Or, for the latest development version:

```sh
git clone https://github.com/alibaba/python-static-analysis-cfg.git
cd python-static-analysis-cfg
pip install .
```

### Build Instructions

To build the project, ensure you have Poetry installed:

```sh
poetry install
poetry build
```

### CLI Command Recipes

```sh
# Basic Usage
python-static-analysis-cfg --help

# Analyze a single file
python-static-analysis-cfg /path/to/file.py

# Analyze a directory
python-static-analysis-cfg /path/to/directory/

# Configure with a custom YAML file
python-static-analysis-cfg --config /path/to/config.yaml

# Output results to a file
python-static-analysis-cfg /path/to/file.py > results.txt
```

## Test Coverage & Benchmark Results

### Test Coverage

`python-static-analysis-cfg` maintains a high level of test coverage, with over 95% of the codebase being tested. The tests are executed using `pytest` and are part of the continuous integration pipeline.

### Benchmark Results

The tool has been benchmarked on a variety of Python projects, ranging from small scripts to large enterprise-scale applications. On average, the analysis process takes less than 10 seconds per 1000 lines of code, making it suitable for real-time analysis.

For more detailed benchmark results, please refer to the project's [benchmarks](https://github.com/alibaba/python-static-analysis-cfg/tree/main/benchmarks) directory.
# AI-Powered Medical Diagnosis: Integrating GPT-4 and Computer Vision

## Project Overview

Welcome to the AI-Powered Medical Diagnosis project! This project leverages the power of GPT-4 for natural language processing and advanced computer vision techniques to provide accurate and efficient medical diagnoses. Follow the instructions below to set up your environment and get started.

### Prerequisites

Before you begin, ensure you have Conda installed on your machine. Conda is essential for managing the project dependencies efficiently.

### Setup Instructions

#### Step 1: Create a New Virtual Environment

First, create a new Conda virtual environment specifically for this project. This helps keep your project dependencies isolated from other projects.

```bash
conda create -n llmapp python=3.10 -y
```

#### Step 2: Activate the Virtual Environment

Activate your new virtual environment to start working with it.

```bash
conda activate llmapp
```
#### Step 3: Install Required Dependencies

After activating the environment, you need to install the required dependencies. This project uses several Python packages, which are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

#### Step 4: Additional Development Dependencies

For development purposes, you might need additional packages listed in `requirements_dev.txt`. Install these by running:

```bash
pip install -r requirements_dev.txt
```

#### Step 5: Initial Setup Script

Run the initial setup script to configure the environment properly:

```bash
bash init_setup.sh
```

# Project Structure

Here is an overview of the project's directory structure:


#### Key Files and Directories

- `src/pipeline/`: Contains the training and prediction pipelines.
- `src/utils/`: Utility functions to support various tasks.
- `src/logger/`: Logging configurations and utilities.
- `src/exception/`: Custom exception handling classes.
- `tests/unit/`: Unit tests for individual components.
- `tests/integration/`: Integration tests for the entire system.
- `init_setup.sh`: Script to initialize the setup.
- `requirements.txt`: List of main dependencies.
- `requirements_dev.txt`: List of development dependencies.
- `setup.py`: Script for setting up the package.
- `setup.cfg`: Configuration file for setup tools.

# Running the Project

Once you have set up the environment and installed all dependencies, you can start running the project. Typically, you will start by running the training pipeline:

```bash
python src/pipeline/training_pipeline.py
```

And then use the prediction pipeline for making predictions:

```bash
python src/pipeline/prediction_pipeline.py
```

# Contributing
We welcome contributions! Please read our CONTRIBUTING.md to learn how you can help improve this project.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact
For any questions or suggestions, feel free to open an issue or contact the project maintainers.
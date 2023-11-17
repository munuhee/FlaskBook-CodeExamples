# Simple Flask App

This repository contains a simple Flask application demonstrating basic setup and usage.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Introduction

This repository serves as a guide for setting up a basic Flask application. It includes steps to create a minimal Flask project structure, define routes, and run the application. Follow the instructions below to get started with Flask!

## Prerequisites

Before getting started, ensure you have the following installed:

- Python (3.6 and above)
- pip (Python package manager)

## Installation

To set up the Flask environment and run the sample app, follow these steps:

1. Navigate to the project directory:

   ```bash
   cd simple-flask-app
   ```

3. Create a virtual environment (recommended):

   ```bash
   # Create a virtual environment named 'myenv'
   python -m venv myenv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```
     myenv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

5. Install Flask and dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Follow these steps to run the Flask application:

1. Ensure you're in the project directory.

2. Run the Flask app:

   ```bash
   python run.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see "Hello, Flask! This is the homepage." displayed on the webpage.

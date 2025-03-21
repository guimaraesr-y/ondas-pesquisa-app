.PHONY: install clean build run setup test env

# Python commands
PYTHON = python
PIP = pip
PYINSTALLER = pyinstaller

# Project settings
APP_NAME = OndasPesquisa
MAIN_FILE = main.py
REQUIREMENTS = requirements.txt

# Virtual environment
VENV = venv
VENV_PYTHON = $(VENV)/Scripts/python
VENV_PIP = $(VENV)/Scripts/pip

# Default target
all: setup install build

# Create virtual environment
env:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
install:
	$(PIP) install -r $(REQUIREMENTS)

# Clean build artifacts
clean:
	@echo "Cleaning build directories..."
	@if exist "build" rd /s /q build
	@if exist "dist" rd /s /q dist
	@if exist "*.spec" del /f /q *.spec
	@if exist "__pycache__" rd /s /q __pycache__
	@echo "Clean completed!"

# Build executable
build:
	$(PYTHON) build.py

# Run the application
run:
	$(PYTHON) $(MAIN_FILE)

# Setup development environment
setup: env
	$(VENV_PIP) install -r $(REQUIREMENTS)

# Run tests (if you add them later)
test:
	$(PYTHON) -m pytest

# Help command
help:
	@echo Available commands:
	@echo   make env      : Create virtual environment
	@echo   make install  : Install dependencies
	@echo   make clean    : Clean build artifacts
	@echo   make build    : Build executable
	@echo   make run      : Run the application
	@echo   make setup    : Setup development environment
	@echo   make test     : Run tests
	@echo   make all      : Setup, install and build 
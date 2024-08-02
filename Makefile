# Variables
PYTHON = python3
PROJECT_NAME = decor8r

# Directories
SOURCE_DIR = $(PROJECT_NAME)
TEST_DIR = test

# Targets
.PHONY: all format check test test_verbose docs run pyinstaller project clean

all: format check test docs

format:
	@echo "Formatting code..."
	$(PYTHON) -m black $(SOURCE_DIR)
	$(PYTHON) -m isort $(SOURCE_DIR)

check:
	@echo "Running mypy for type checking..."
	$(PYTHON) -m mypy $(SOURCE_DIR)

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest $(TEST_DIR)

test-verbose:
	@echo "Running tests with verbose output..."
	$(PYTHON) -m pytest -v $(TEST_DIR)

run:
	@echo "Running the application..."
	$(PYTHON) -m $(SOURCE_DIR).server

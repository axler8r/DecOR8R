# Variables
PYTHON = python3

# Directories
SOURCE_DIR = source
TEST_DIR = test

# Targets
.PHONY: all format check test test_verbose docs run pyinstaller project clean

all: format check test docs

format:
	@echo "Formatting code..."
	ruff format $(SOURCE_DIR) $(TEST_DIR)

check:
	@echo "Checking code..."
	ruff check $(SOURCE_DIR) $(TEST_DIR)

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest $(TEST_DIR)

test-verbose:
	@echo "Running tests with verbose output..."
	$(PYTHON) -m pytest -v $(TEST_DIR)

run:
	@echo "Running the application..."
	$(PYTHON) -m $(SOURCE_DIR).server

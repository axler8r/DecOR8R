# Variables
PYTHON = python3
PROJECT_NAME = decor8r

# Directories
BIN_DIR = bin
DIST_DIR = dist
DOC_DIR = doc
SRC_DIR = $(PROJECT_NAME)
TEST_DIR = test

# Targets
.PHONY: all format check test test_verbose docs run pyinstaller project clean

all: format check test docs

format:
	@echo "Formatting code..."
	$(PYTHON) -m black $(SRC_DIR)
	$(PYTHON) -m isort $(SRC_DIR)

check:
	@echo "Running mypy for type checking..."
	$(PYTHON) -m mypy $(SRC_DIR)

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest $(TEST_DIR)

test_verbose:
	@echo "Running tests with verbose output..."
	$(PYTHON) -m pytest -v $(TEST_DIR)

docs:
	@echo "Generating documentation..."
	cd $(DOC_DIR) && $(MAKE) html

run:
	@echo "Running the application..."
	$(PYTHON) -m $(SRC_DIR).main  # Replace 'main' with the name of your entry point file

pyinstaller:
	@echo "Creating standalone executables..."
	$(PYTHON) -m PyInstaller $(SRC_DIR)/main.py --name $(PROJECT_NAME) --distpath $(DIST_DIR) --clean --onefile

clean:
	@echo "Cleaning up..."
	rm -rf $(DOC_DIR)/build
	rm -rf $(DIST_DIR)

# Variables
PYTHON = python3

# Directories
SOURCE_DIR = source
TEST_DIR = test

# Targets
.PHONY: all format check test test_verbose docs run pyinstaller project clean

all: format check test docs
clean:
	@echo "Cleaning up..."
	rm -rf **/__pycache__ 2>/dev/null
	rm -r  **/*.pyc 2>/dev/null

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

start-server:
	@echo "Running the application..."
	[ -d log ] || mkdir log
	PYTHONPATH=$(shell pwd)/source/:${PYTHONPATH} nohup $(PYTHON) -m decor8rd.server > log/server-$(shell date +%Y%m%d%H%M%S).log &

stop-server:
	@echo "Stopping the application..."
	echo stop | nc -U /tmp/decor8r.sock

send-request:
	@echo "Sending a request to the server..."
	echo $(filter-out $@,$(MAKECMDGOALS)) | nc -U /tmp/decor8r.sock && echo


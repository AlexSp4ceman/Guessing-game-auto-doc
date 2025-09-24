# Makefile for Python Guessing Game Project
# Cross-platform compatible Makefile

# Variables
PYTHON = python
PIP = pip
DOC_FILE = Guessing_Game_Documentation.docx
REQUIREMENTS = requirements.txt

# Detect operating system
ifeq ($(OS),Windows_NT)
    DETECTED_OS = Windows
    RM = del /Q
    MKDIR = mkdir
    RMDIR = rmdir /S /Q
else
    DETECTED_OS = $(shell uname -s)
    RM = rm -f
    MKDIR = mkdir -p
    RMDIR = rm -rf
endif

# Default target
all: help

# Help target - show available commands
help:
	@echo "Python Guessing Game Project - Available Commands:"
	@echo ""
	@echo "  install     - Install required dependencies"
	@echo "  run         - Run the guessing game"
	@echo "  docs        - Generate documentation from code comments"
	@echo "  clean       - Remove generated documentation"
	@echo "  clean-all   - Remove all generated files"
	@echo "  test        - Run a quick functionality test"
	@echo "  help        - Show this help message"
	@echo ""
	@echo "Detected OS: $(DETECTED_OS)"

# Install dependencies
install:
	@echo "Installing dependencies from $(REQUIREMENTS)..."
	$(PIP) install -r $(REQUIREMENTS)
	@echo "Dependencies installed successfully!"

# Run the guessing game
run:
	@echo "Starting Guessing Game..."
	$(PYTHON) guessing_game.py

# Generate documentation
docs:
	@echo "Generating documentation from code comments..."
	$(PYTHON) documentation_generator.py

# Clean generated documentation
clean:
	@echo "Cleaning up generated documentation..."
ifeq ($(DETECTED_OS),Windows)
	if exist $(DOC_FILE) $(RM) $(DOC_FILE) && echo "Documentation deleted"
else
	if [ -f "$(DOC_FILE)" ]; then $(RM) "$(DOC_FILE)" && echo "Documentation deleted"; fi
endif

# Clean all generated files
clean-all: clean
	@echo "Cleaning all generated files..."
ifeq ($(DETECTED_OS),Windows)
	if exist __pycache__ $(RMDIR) __pycache__
	if exist *.pyc $(RM) *.pyc
else
	if [ -d "__pycache__" ]; then $(RMDIR) __pycache__; fi
	$(RM) *.pyc
endif
	@echo "All generated files cleaned!"

# Test the application functionality
test:
	@echo "Running quick functionality test..."
	@echo "1. Testing Python installation..."
	$(PYTHON) --version
	@echo "2. Testing dependencies..."
	$(PYTHON) -c "import docx; print('python-docx is available')"
	@echo "3. Testing game import..."
	$(PYTHON) -c "from guessing_game import GuessingGame; print('GuessingGame imports successfully')"
	@echo "4. Testing documentation generator import..."
	$(PYTHON) -c "from documentation_generator import DocumentationGenerator; print('DocumentationGenerator imports successfully')"
	@echo "All tests passed!"

# Development setup (install in development mode)
dev: install test
	@echo "Development environment is ready!"

# Full build process
build: install test docs
	@echo "Build process completed successfully!"

# Show project information
info:
	@echo "Project Information:"
	@echo "===================="
	@echo "Python Version: $$($(PYTHON) --version)"
	@echo "Operating System: $(DETECTED_OS)"
	@echo "Available Python files:"
	@dir *.py 2>nul || ls *.py 2>/dev/null || echo "No Python files found"
	@echo "Generated files:"
ifeq ($(DETECTED_OS),Windows)
	@if exist $(DOC_FILE) echo "  - $(DOC_FILE)" || echo "  - No documentation file found"
else
	@if [ -f "$(DOC_FILE)" ]; then echo "  - $(DOC_FILE)"; else echo "  - No documentation file found"; fi
endif

# Phony targets (targets that are not files)
.PHONY: all help install run docs clean clean-all test dev build info
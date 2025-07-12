# uv Package Management Cheatsheet

## Installation

```bash
# Install uv (recommended method)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv

# Or via pipx
pipx install uv
```

## Project Management

### Initialize & Create Projects
```bash
# Create a new Python project
uv init my-project
uv init --python 3.11 my-project  # Specify Python version

# Initialize in existing directory
uv init

# Create with specific template
uv init --template minimal my-project
```

### Python Version Management
```bash
# Install Python versions
uv python install 3.11
uv python install 3.12

# List available Python versions
uv python list

# Set project Python version
uv python pin 3.11
```

## Dependency Management

### Adding Dependencies
```bash
# Add a dependency
uv add requests
uv add "django>=4.0"

# Add development dependencies
uv add --dev pytest black

# Add optional dependencies
uv add --optional docs sphinx

# Add from git
uv add git+https://github.com/user/repo.git
```

### Removing Dependencies
```bash
# Remove a dependency
uv remove requests

# Remove dev dependency
uv remove --dev pytest
```

### Installing Dependencies
```bash
# Install all dependencies
uv sync

# Install only production dependencies
uv sync --no-dev

# Install with specific groups
uv sync --group docs
```

## Virtual Environment Management

### Creating & Managing Environments
```bash
# Create virtual environment
uv venv

# Create with specific Python version
uv venv --python 3.11

# Activate environment (manual)
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Deactivate environment
deactivate

# Run commands in environment
uv run python script.py
uv run pytest
```

## Package Installation (pip replacement)

### Installing Packages
```bash
# Install packages
uv pip install requests
uv pip install -r requirements.txt

# Install from PyPI
uv pip install "django>=4.0,<5.0"

# Install from git
uv pip install git+https://github.com/user/repo.git

# Install in editable mode
uv pip install -e .
```

### Listing & Information
```bash
# List installed packages
uv pip list

# Show package information
uv pip show requests

# Check outdated packages
uv pip list --outdated
```

### Uninstalling
```bash
# Uninstall package
uv pip uninstall requests

# Uninstall all packages
uv pip freeze | uv pip uninstall -r /dev/stdin
```

## Lock Files & Reproducibility

### Lock File Management
```bash
# Generate lock file
uv lock

# Update lock file
uv lock --upgrade

# Install from lock file
uv sync --frozen
```

### Export Requirements
```bash
# Export to requirements.txt
uv export --format requirements-txt > requirements.txt

# Export dev dependencies
uv export --dev --format requirements-txt > dev-requirements.txt
```

## Running Scripts & Commands

### Script Execution
```bash
# Run Python script
uv run python script.py

# Run with arguments
uv run python script.py --arg value

# Run tools
uv run black .
uv run pytest tests/
uv run mypy src/
```

### Tool Installation & Running
```bash
# Install and run tool globally
uv tool install black
uv tool run black .

# Run tool without installing
uv tool run ruff check .
```

## Configuration

### pyproject.toml Configuration
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
dependencies = [
    "requests>=2.28.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
    "ruff>=0.1.0",
]
docs = [
    "sphinx>=5.0",
    "sphinx-rtd-theme>=1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=7.0",
    "black>=22.0",
]
```

### Environment Variables
```bash
# Set cache directory
export UV_CACHE_DIR=/path/to/cache

# Set index URL
export UV_INDEX_URL=https://pypi.org/simple

# Disable cache
export UV_NO_CACHE=1
```

## Common Workflows

### New Project Setup
```bash
# Complete new project setup
uv init my-project
cd my-project
uv add requests click
uv add --dev pytest black ruff
uv sync
```

### Existing Project Setup
```bash
# Clone and setup existing project
git clone https://github.com/user/project.git
cd project
uv sync
```

### Dependency Updates
```bash
# Update all dependencies
uv lock --upgrade
uv sync

# Update specific package
uv add requests --upgrade
```

### Development Workflow
```bash
# Install dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .
```

## Performance & Caching

### Cache Management
```bash
# Clear cache
uv cache clean

# Show cache info
uv cache dir

# Cache size
uv cache size
```

### Parallel Installation
```bash
# Install with specific number of threads
uv pip install -r requirements.txt --jobs 4
```

## Comparison with Traditional Tools

| Task | Traditional | uv |
|------|-------------|-----|
| Create venv | `python -m venv .venv` | `uv venv` |
| Install package | `pip install requests` | `uv pip install requests` |
| Install from requirements | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| Add dependency | Edit requirements.txt manually | `uv add requests` |
| Update dependencies | `pip install --upgrade -r requirements.txt` | `uv lock --upgrade && uv sync` |

## Tips & Best Practices

1. **Use `uv sync` instead of `pip install -r requirements.txt`** for better dependency resolution
2. **Pin Python versions** with `uv python pin` for reproducible builds
3. **Use lock files** for production deployments with `uv sync --frozen`
4. **Leverage `uv run`** to execute scripts without manual environment activation
5. **Use `uv tool run`** for one-off tool execution without global installation
6. **Keep pyproject.toml** as the single source of truth for dependencies
7. **Use dependency groups** to organize different types of dependencies (dev, docs, etc.)

## Common Flags

- `--python`: Specify Python version
- `--dev`: Target development dependencies
- `--frozen`: Use exact versions from lock file
- `--upgrade`: Upgrade to latest compatible versions
- `--no-cache`: Disable cache usage
- `--verbose`: Show detailed output
- `--quiet`: Suppress output
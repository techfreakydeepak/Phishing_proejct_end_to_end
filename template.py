import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/.gitkeep",
    'src/__init__.py',
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_curd.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",  # Corrected typo here
    "tests/integration/int.py",  # Corrected typo here
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",  # Added missing comma
    "setup.cfg",  # Added missing comma
    "pyproject.toml",  # Corrected file name and added missing comma
    "tox.ini",
    "experiments/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Corrected usage
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file

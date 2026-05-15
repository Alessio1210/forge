import ast
import os
import sys
from importlib.metadata import packages_distributions
from pathlib import Path


def create_requirements_file():
    root = Path.cwd()
    used_libs = set()

    installed_packages = packages_distributions()

    local_modules = {path.stem for path in root.glob("*.py")} | {
        path.name
        for path in root.iterdir()
        if path.is_dir() and path.name not in [".venv", "__pycache__"]
    }

    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in [".venv", "__pycache__", ".git"]]

        for file in files:
            if not file.endswith(".py"):
                continue

            file_path = Path(current_root) / file

            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        used_libs.add(name.name.split(".")[0])

                elif isinstance(node, ast.ImportFrom):
                    if node.level == 0 and node.module:
                        used_libs.add(node.module.split(".")[0])

    external_libs = set()

    for lib in used_libs:
        if lib in sys.stdlib_module_names:
            continue

        if lib in local_modules:
            continue

        package_names = installed_packages.get(lib)

        if package_names:
            external_libs.update(package_names)
        else:
            external_libs.add(lib)

    requirements_path = root / "requirements-dev.txt"

    with open(requirements_path, "w", encoding="utf-8") as f:
        for lib in sorted(external_libs):
            f.write(lib + "\n")

    print(f"Created {requirements_path}")


if __name__ == "__main__":
    create_requirements_file()

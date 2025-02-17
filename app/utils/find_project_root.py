from pathlib import Path

def find_project_root():
    # Look for a specific file like README.md, .git, or pyproject.toml
    current_dir = Path(__file__).resolve().parent
    while current_dir != current_dir.parent:
        if any((current_dir / marker).exists() for marker in ["README.md", "pyproject.toml"]):
            return current_dir
        current_dir = current_dir.parent
    raise FileNotFoundError("Project root not found")

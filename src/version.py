# src/version.py
import os
from importlib.metadata import PackageNotFoundError, version as _get_installed_version
from pathlib import Path
import tomllib  # Python 3.11+; use tomli for older versions

def _read_pyproject_version(pyproject_path: Path) -> str | None:
    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)
        # PEP 621: project.version or tool.poetry.version etc.
        proj = data.get("project")
        if proj and "version" in proj:
            return proj["version"]
        # common alternative for Poetry
        poetry = data.get("tool", {}).get("poetry")
        if poetry and "version" in poetry:
            return poetry["version"]
    except Exception:
        return None

def get_version(package_name: str, default: str = "0.0.0-dev") -> str:
    # 1) env override
    env = os.getenv("PROJECT_VERSION")
    if env:
        return env

    # 2) installed package metadata
    try:
        return _get_installed_version(package_name)
    except PackageNotFoundError:
        pass

    # 3) read pyproject.toml in repo root (best effort)
    repo_root = Path(__file__).resolve().parents[1]  # adjust if layout differs
    pyproject = repo_root / "pyproject.toml"
    py_ver = _read_pyproject_version(pyproject) if pyproject.exists() else None
    if py_ver:
        return py_ver

    # 4) fallback
    return default

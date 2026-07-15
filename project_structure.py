# ==========================================================
# Create SwaraFormer Project Structure
# ==========================================================

from pathlib import Path

# Change this path if your repository is cloned elsewhere
PROJECT_DIR = Path("D:\\Research\\SwaraFormer")

folders = [
    "notebooks",

    "configs",

    "models",
    "utils",

    "dataset",
    "dataset/raw",
    "dataset/subset",
    "dataset/processed",
    "dataset/embeddings",

    "checkpoints",

    "results",
    "results/figures",
    "results/logs",
    "results/confusion_matrix",

    "docs"
]

# Create folders
for folder in folders:
    (PROJECT_DIR / folder).mkdir(parents=True, exist_ok=True)

# Create empty Python files
python_files = [
    "models/__init__.py",
    "models/encoder.py",
    "models/transformer.py",
    "models/bilstm.py",
    "models/conformer.py",
    "models/fusion.py",
    "models/blocks.py",

    "utils/__init__.py",
    "utils/audio.py",
    "utils/feature_extraction.py",
    "utils/dataset.py",
    "utils/metrics.py",
    "utils/train.py",
    "utils/visualization.py",

    "configs/config.py"
]

for file in python_files:
    path = PROJECT_DIR / file
    path.touch(exist_ok=True)

# Create README if it doesn't exist
readme = PROJECT_DIR / "README.md"

if not readme.exists():
    readme.write_text(
"""# SwaraFormer

A Multi-Modal Deep Learning Framework for Automatic Swara Recognition.

## Repository Structure

- notebooks/
- models/
- utils/
- dataset/
- checkpoints/
- results/
"""
    )

print("="*60)
print("SwaraFormer project structure created successfully!")
print("="*60)

# Display the directory tree
for path in sorted(PROJECT_DIR.rglob("*")):
    depth = len(path.relative_to(PROJECT_DIR).parts)
    indent = "    " * (depth - 1)
    print(f"{indent}{path.name}")
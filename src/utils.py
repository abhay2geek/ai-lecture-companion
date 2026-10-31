from pathlib import Path

def ensure_directories():
    # Ensure that all necessary directories exist
    directories = [
        Path("data/input"),
        Path("data/audio"),
        Path("data/frames"),
        Path("data/processed"),
        Path("output"),
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
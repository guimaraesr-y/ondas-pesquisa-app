import os
import shutil
import PyInstaller.__main__
import qt_material


def clean_build_directories():
    """Clean up build directories before creating new build"""
    directories = ["build", "dist"]
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        if os.path.exists(f"{directory}.spec"):
            os.remove(f"{directory}.spec")


def get_qt_material_path():
    """Get the path to qt_material package data"""
    return os.path.dirname(qt_material.__file__)


def build_executable():
    """Build the executable using PyInstaller"""
    qt_material_path = get_qt_material_path()

    command = [
        "main.py",
        "--name=OndasPesquisa",
        "--onefile",
        "--windowed",
        f"--add-data={qt_material_path};qt_material",
        "--add-data=logo.png;.",
        "--clean",
        "--noconfirm",
    ]

    PyInstaller.__main__.run(command)


if __name__ == "__main__":
    clean_build_directories()
    build_executable()
    print("Build completed! Check the 'dist' folder for your executable.")

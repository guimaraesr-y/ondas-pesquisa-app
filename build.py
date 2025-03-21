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

    # Build command without icon by default
    command = [
        "main.py",
        "--name=OndasPesquisa",
        "--onefile",
        "--windowed",
        f"--add-data={qt_material_path};qt_material",
        "--clean",
        "--noconfirm",
        # Add hidden imports to fix qt_material warning
        "--hidden-import=PyQt6.QtCore",
        "--hidden-import=PyQt6.QtGui",
        "--hidden-import=PyQt6.QtWidgets",
        "--hidden-import=qt_material"
    ]

    # Only add icon if it exists and is valid
    if os.path.exists("app_icon.ico") and os.path.getsize("app_icon.ico") > 0:
        command.append("--icon=app_icon.ico")

    PyInstaller.__main__.run(command)


if __name__ == "__main__":
    clean_build_directories()
    build_executable()
    print("Build completed! Check the 'dist' folder for your executable.")

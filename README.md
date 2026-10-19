# Calculator

A calculator self-project in which you can calculate sums, differences, products, and quotients, exponents, roots, compare numbers, and work with percentages, including profit and loss and simple interest. Made by Arihaan Yadav.

## Easy way to open

Want to open the app the easy way and be lazy to even open cmd? YEs, then open the [`open_app`](./open_app) folder and use the launcher for your operating system:

- **Windows:** double-click [`open.bat`](./open_app/open.bat).
- **macOS:** double-click [`open.command`](./open_app/open.command).
- **Linux:** open a terminal in the `open_app` folder and run `bash open.sh`.

These launch the calculator in a terminal. Python must be installed first. Windows needs `python` available in PATH; macOS and Linux need `python3`.

## Requirements

Python 3 is required. Install it with the package manager for your platform:

### Windows (winget)

```powershell
winget install Python.Python.3.13
```

### Windows (Scoop)

```powershell
scoop install python
```

### macOS (Homebrew)

```sh
brew install python
```

### Linux

Use your distribution's package manager. For example:

```sh
# Ubuntu or Debian
sudo apt update
sudo apt install python3

# Fedora
sudo dnf install python3

# Arch Linux
sudo pacman -S python
```

## Run from a terminal

You can also download or clone this repository, open a terminal in the project folder, and run:

```sh
python main.py
```

On Linux and macOS, use `python3` if `python` does not point to Python 3:

```sh
python3 main.py
```

Choose an option from the menu to use the calculator, number comparison, squares, roots, or percentage tools.

## Optional desktop shortcut

To create a desktop icon or launcher, run [`create_shortcut.vbs`](./open_app/create_shortcut.vbs) on Windows. On macOS or Linux, run `bash create_shortcut.sh` from the `open_app` folder.

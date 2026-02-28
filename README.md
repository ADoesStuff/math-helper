# Math helper

Math helper is a Python program designed to teach you basic multiplication (e.g. 6x11)

It does this by giving you quizes that you need to answer untill you start getting them right.

# How to run

To launch the program simply use run.bat (for windows) or run.sh (for linux).

# How to convert into an executable

### For Windows

You need to have python 3.12, as of the time this is being written the latest python version **WILL NOT** work.
You will then need to install Nuitka, for further detail go [here](https://nuitka.net/doc/download.html). 
Then you will need to run the ``pack.bat`` file and if the resulting executable gets blocked by windows security simply disable real time protection.

### For Linux

You will need Python 3.12 (or above), to install Python you must run ``sudo apt-get install python3`` for debian based distros, ``sudo pacman -S python3``for arch based distros and ``sudo dnf install python3`` for fedora or fedora based distros.
You will then need to install Nuitka, for further detail go [here](https://nuitka.net/doc/download.html). 
Then you will need to run ``pack.sh``.
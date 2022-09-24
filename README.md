**Still a work in progress**

A MacOS menubar app for [devmarks](https://devmarks.io). Will show the current number of bookmarks for a user and allow someone to easily add a new bookmark to their account.

# How to develop the app

`rumps` is used for creating the menubar app.

`poetry run devmarks` (or `poetry run python devmarks_menubar/main.py`) will start the app for troubleshooting, but alerts and windows will open behind every other app which is super annoying (once built with `py2app` this doesn't happen).

# How to build the app

[`py2app`](https://py2app.readthedocs.io/) is used to build a standalone MacOS app. Python 3.9 is required -- using Python 3.10 won't build properly.

If `~/.pyenv/versions/3.9.x/lib/libpython3.9.dylib` is missing, you'll need to install a Python version: `PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.9.x`

## Build
`poetry run python3 setup.py py2app`

## Run the menubar
Double-click on `dist/Devmarks` in the Finder.

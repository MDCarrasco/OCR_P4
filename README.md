# OCR_P4

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107670243-d3d66400-6c92-11eb-9bc0-10294308cb0b.png">
OpenClassrooms' Python Project 4 (Chess Yo Self) is an Python MVC interactive CLI chess tournament manager using tinyDB.

Front is a mix of simple-term-menu and pydoc packages.

Therefore it only works on UNIX.

## Installation

```shell-session
python -m venv env
source ./env/bin/activate
pip install -r ./requirements.txt
```

## Usage

### Launch

```shell-session
./run
```

### Logs
```shell-session
./clearlogs
./seelogs
```

### Flake8 Report
```shell-session
./runflake8
```
Logs can be found in the "logs" folder, flake8-html report is located inside the "flake8-rapport" folder and it has option max-line-length set to 119.

## How it works

- ### "Why is it locked ?/Why is my form stuck when I try to submit an input ?"

When you load an empty database file or create a new one, there are some options not yet available to you.  
For example you will not be able to create a tournament event if you have no players stored in the selected DB (in fact you need at least 3).  
You will not be able to change a player's rank if you don't have any player stored.  
You will get an error message (bottom line of your term window) when trying to submit a tournament date prior to today's date etc etc...  

Got it ?

- ### Loading a database file/Creating a new database

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107674742-92948300-6c97-11eb-8262-b9d289be4865.gif">
When you first run the program you will be asked to load a database, this is mandatory and cannot be skipped ofc.

You may then create a new database file if you so desire.

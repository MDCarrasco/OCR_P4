# OCR_P4

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107670243-d3d66400-6c92-11eb-9bc0-10294308cb0b.png">
OpenClassrooms' Python Project 4 (Chess Yo Self) is an Python MVC interactive CLI chess tournament manager using tinyDB.

Front is a mix of simple-term-menu and pydoc packages.

Therefore it only works on UNIX.

- [Installation](#installation)
- [Usage](#usage)
  * [Launch](#launch)
  * [Logs](#logs)
  * [Flake8 Report](#flake8-report)
- [How it works](#how-it-works)
  * ["Why is it locked ?/Why is my form stuck when I try to submit an input ?"](#-why-is-it-locked---why-is-my-form-stuck-when-i-try-to-submit-an-input---)
  * [Load a database file/Create a new database](#load-a-database-file-create-a-new-database)
  * [Add a new player](#add-a-new-player)
  * [Change a player's rank](#change-a-player-s-rank)
  * [Schedule a tournament](#schedule-a-tournament)
  * [Start a tournament](#start-a-tournament)
  * [Display match history](#display-match-history)
  * [Display logs](#display-logs)
- [Notes](#notes)

## Installation

```bash
python3 -m venv env
source ./env/bin/activate
pip3 install -r ./requirements.txt
```

## Usage

### Launch

```bash
./run
```

### Logs
```bash
./clearlogs
./seelogs
```

### Flake8 Report
```bash
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

- ### Load a database file/Create a new database

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107674742-92948300-6c97-11eb-8262-b9d289be4865.gif">
When you first run the program you will be asked to load a database, this is mandatory and cannot be skipped ofc.

You may then create a new database file if you so desire.

- ### Add a new player

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107677012-10f22480-6c9a-11eb-9b18-62cf06cd425f.gif">
<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107677706-da68d980-6c9a-11eb-9994-0ee5d6adc37c.gif">
If you try to register a player with the same rank as the one of a player in database you may get an error like this one.

- ### Change a player's rank

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107679570-02f1d300-6c9d-11eb-9b39-034c6d95cf1a.gif">
Once you got at least one player registered you can now edit it's rank at will.  
If the player goes up in rank, all players that are between it's new rank and it's old one will go down in rank.  
If the player goes down in rank, all... you get it.

- ### Schedule a tournament

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107680568-4d278400-6c9e-11eb-9bd3-16476297ab0b.gif">
<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107680777-95df3d00-6c9e-11eb-91d7-239c7e343d02.gif">
Simple, you fill in the form and that's it.  
You can check whether all is good via the "Afficher" (Display) menu.

- ### Start a tournament

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107683173-8a414580-6ca1-11eb-9bd2-c8900ec91d8d.gif">
FINALLY ! You have at least 3 players registered and a tournament scheduled. Time to play the game.<br />
All you have to do is tell "Chess yo self" who won or if this is a tie.<br />
(THIS DOES NOT WORK CURRENTLY).<br />
Matchmaking follows the swiss-system.<br />
If there are an uneven number of players, then players may get one point from playing against no one during a round.<br />
You get to see the winner's cup at the end.

- ### Display match history

<img width="490" alt="image" src="https://user-images.githubusercontent.com/50454011/107683777-43a01b00-6ca2-11eb-91c4-886a12653e46.gif">
You can consult the rounds and matches details afterwards.

- ### Display logs
 
If you wish to do so, you can display the log pages generated by "Chess yo self" throuhout the entire duration of it's usage.

## Notes

I had a hard time with this project and I'm still struggling with some parts of it as I type this markdown.  
No to little help during the whole process of coding this.  
Sadly I must move on with my formation, I learned some stuff about MVC though it's not perfect.   

## TODO (fix)

Tournaments should be played only once.   
Matchmaking does not work.

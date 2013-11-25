skypebot
========
Proof of concept bot for Skype containing a variety of different games and functions.

Dependencies
------------
* Skype4Py
* pickledb

Features
--------
This bot currently includes the following:

* Trivia
* Word Shuffle
* 8Ball
* Dictionary
* Google Results
* League of Legends counter picks
* Link Cataloging

Usage
-----
Requires Skype to be running, simply running bot.py will initialize the bot and focus the Skype window. Skype will ask you if you wish to allow access to the script (python.exe).

A List of available commands can be viewed by entering the following command in a Skype chat window: !commands

Example Commands
----------------
!question - Starts the trivia bot

!shuffle - Starts the word shuffle bot

!stop - Stops both trivia/shuffle questions

!8b <query> - 8ball response

!define <query> - Dictionary look-up

!google <query> - Returns top 5 google search results

!cadd <category> <url> - Stores a url in specified <category>

!cget <category> - Returns all stored urls in the specified <category>

!cata - Returns all active categories


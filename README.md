# Mood Tracker Bot

A Telegram bot serve as a mood tracker. Help you fight for depression, enhance your life...

> A simple private bot with this idea served as my loyal bot for a year. This project I remaked base on it, added some magic, start open source.

**Why you need a mood chart?**

> The tricky thing about moods is that they are transitory, and can come and go without warning, cause, or reason. This is why, unlike emotions, which arise due to, or as a result of, specific events, moods represent our overall state, and determine how we interpret or approach external stimuli. Also, they can last much longer than emotions. (Mood, 2015)
> 
> One’s personality can influence the way a mood is displayed, and the actions that one takes during such phases. 
> 
> That’s why, the purposeful act of widening our attention to spot positive stimuli not only helps us maintain our positive affect, but provides us with more resources by which to refer back to it. (Wadlinger and Isaacowitz, 2006)

**This project is under heavy develope! Not available for end user.**

## Usage

* Clone this repo
* Install with ...
* WIP

## Messages

* `/today`: Put down your mood here.
* `/report`: Get a report of your mood in 7 days.
* `/pixel`: Your life in a pixel.

## Developement

### Stack

* Python 3.7
* Postgres
* SQLAlchemy, Alembic
* `python-bot-framework`
* `pandas`, `matplotlib`

### Commands

Usage: `./make.sh <command> [<subcommand>]`

* `run`: start project
* `migrate`: miration tasks
    * `gen`: Auto generate migration
    * `upgrade`: Upgrade head migration

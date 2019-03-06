# Personal Finance Bot

A Telegram bot help you keep track your expense, budgets, visualize your wallet and keep your personal finance under control. :moneybag:

**This project is under heavy develope! Not available for enduser.**

## Usage

* Clone this repo
* WIP

## Messages

* `/ping`: Check your bot status.
* `/report`: Get a report of your personal finance.
* Add a expense to keep track. WIP doc.

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

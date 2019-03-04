# Personal Finance Bot

A Bot helper keep track your expense, visualize and keep your personal finance undercontrol.

## Prerequisites

* Python

## Usage

* Clone this repo

## Message Handle

* `/ping`
* `<money amount> <category> [<timestamp>] <note...>`
    * `<money amount>`: Can be `20k`, `20.5k`, `20500` , `20.500` (using `-` or `+` to define it's a income or expense, parse as expense if ommit)
    * `category`: A single word
    * `<timestamp>`: Can be `@1d`, `@2d`
    * `<note...>`: All words after is a note

## Developement

### Techstack

* Python 3.7
* Postgres
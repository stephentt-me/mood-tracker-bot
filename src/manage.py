from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)

import click

from src.models import *
from src.models.base import Base

@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')
    Base.metadata.create_all()

@click.command()
def dropdb():
    click.echo('Dropped the database')
    Base.metadata.drop_all()

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == "__main__":
    cli()

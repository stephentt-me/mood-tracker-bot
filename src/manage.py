from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)

import click

@click.group()
def cli():
    pass

@click.command()
def seed_sample_data():
    click.echo('Seed sample data.')

cli.add_command(seed_sample_data)

if __name__ == "__main__":
    cli()

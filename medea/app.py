import click
from db import init_app_db

@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
@click.option('--count', '-c', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def goodbye(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('goodbye %s!' % name)

@click.group()
def cli():
    pass

if __name__ == '__main__':
    init_app_db()
    cli.add_command(hello)
    cli.add_command(goodbye)
    cli()
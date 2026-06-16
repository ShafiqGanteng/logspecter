import click

from .analyzer import LogAnalyzer
from .dashboard import show_dashboard
from .reporter import export_json


@click.group()
def cli():
    pass


@cli.command()
@click.argument("logfile")
@click.option(
    "--json",
    "json_file",
    default=None
)
def analyze(logfile, json_file):

    analyzer = LogAnalyzer()

    analyzer.analyze(logfile)

    result = analyzer.get_summary()

    show_dashboard(result)


    if json_file:
        export_json(
            result,
            json_file
        )

        click.echo(
            f"Report saved: {json_file}"
        )


if __name__ == "__main__":
    cli()
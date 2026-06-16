from rich.console import Console
from rich.table import Table

console = Console()


def show_dashboard(summary):

    table = Table(title="LogSpecter")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Total Lines",
        str(summary["total_lines"])
    )

    for level, count in summary["levels"].items():

        table.add_row(
            level,
            str(count)
        )

    console.print(table)
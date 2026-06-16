#!/usr/bin/env python3

from pathlib import Path

from logspecter.analyzer import LogAnalyzer
from logspecter.dashboard import show_dashboard


def main():

    log_file = Path(
        "examples/sample.log"
    )

    if not log_file.exists():

        print(
            "Log file tidak ditemukan:"
            f" {log_file}"
        )

        return


    analyzer = LogAnalyzer()

    analyzer.analyze(
        log_file
    )

    result = analyzer.get_summary()

    show_dashboard(
        result
    )


if __name__ == "__main__":
    main()
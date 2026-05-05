import argparse

from reports.clickbait import ClickbaitReport

REPORTS = {
    "clickbait": ClickbaitReport,
}


def parse_args():
    parser = argparse.ArgumentParser(description="YouTube metrics report generator")

    parser.add_argument(
        "--files", nargs="+", required=True, help="Path(s) to the CSV data file(s)"
    )

    parser.add_argument(
        "--report",
        choices=REPORTS.keys(),
        required=True,
        help="Type of report to generate",
    )

    return parser.parse_args()

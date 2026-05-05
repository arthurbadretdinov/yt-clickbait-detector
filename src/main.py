from cli import parse_args, REPORTS
from core.reader import read_csv_files
from core.formatter import format_clickbait_report


def main() -> None:
    args = parse_args()

    data = read_csv_files(args.files)

    report = REPORTS[args.report]

    result = report.generate(data)

    output = format_clickbait_report(result)

    print(output)


if __name__ == "__main__":
    main()

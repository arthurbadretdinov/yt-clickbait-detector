from cli import parse_args, REPORTS
from core.reader import read_csv_files
from core.formatter import format_clickbait_report


def main() -> None:
    try:
        args = parse_args()

        data = read_csv_files(args.files)

        report = REPORTS[args.report]

        result = report.generate(data)

        output = format_clickbait_report(result)

        print(output)

    except FileNotFoundError as e:
        print(f"[ERROR] {e}")

    except ValueError as e:
        print(f"[ERROR] {e}")

    except Exception as e:
        print(f"[UNEXPECTED ERROR] {e}")


if __name__ == "__main__":
    main()

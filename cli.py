import argparse

from execution_metrics import (
    EXECUTION_FILE,
    DEFECT_FILE,
    calculate_execution_totals,
    calculate_completion_percentage,
    calculate_defect_totals,
)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate test execution and defect metrics."
    )
    parser.add_argument(
        "--executions",
        default=EXECUTION_FILE,
        help="Path to the test execution CSV file.",
    )
    parser.add_argument(
        "--defects",
        default=DEFECT_FILE,
        help="Path to the defect CSV file.",
    )
    parser.add_argument(
        "--report",
        choices=("all", "executions", "defects"),
        default="all",
        help="Choose which metrics to display.",
    )

    args = parser.parse_args()

    try:
        if args.report in ("all", "executions"):
            totals = calculate_execution_totals(args.executions)
            total = sum(totals.values())
            completion = calculate_completion_percentage(totals)

            print("\n=== TEST EXECUTION RESULTS ===")
            print(f"Pass:        {totals['pass']}")
            print(f"Fail:        {totals['fail']}")
            print(f"Blocked:     {totals['blocked']}")
            print(f"Not Started: {totals['not_started']}")
            print(f"Total:       {total}")
            print(f"Completion:  {completion:.2f}%")

        if args.report in ("all", "defects"):
            defects = calculate_defect_totals(args.defects)

            print("\n=== DEFECT RESULTS ===")
            for status, count in sorted(defects.items()):
                print(f"{status:<20} {count}")

            print(f"{'Total defects:':<20} {sum(defects.values())}")

    except (OSError, csv.Error, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    import csv
    main()

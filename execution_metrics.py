import csv
from pathlib import Path

# CSV file locations, relative to the project root.
EXECUTION_FILE = "data/executions.csv"
DEFECT_FILE = "data/defects.csv"

EXECUTION_STATUSES = ("pass", "fail", "blocked", "not_started")


def read_csv_file(file_path):
    """Read a CSV file and return its rows as dictionaries."""
    with open(file_path, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def calculate_execution_totals(file_path):
    """Calculate execution totals by result."""
    executions = read_csv_file(file_path)

    totals = dict.fromkeys(EXECUTION_STATUSES, 0)

    for execution in executions:
        result = (
            execution.get("Execution.Result") or ""
        ).strip().lower()

        if result in ("pass", "fail", "blocked"):
            totals[result] += 1
        elif result == "":
            totals["not_started"] += 1

    return totals


def calculate_completion_percentage(totals):
    """Return the percentage of executions that have been attempted."""
    total = sum(totals.values())

    if total == 0:
        return 0.0

    completed = (
        totals["pass"] + totals["fail"] + totals["blocked"]
    )
    return round((completed / total) * 100, 2)


def calculate_defect_totals(file_path):
    """Calculate defect totals grouped by Jira status."""
    defects = read_csv_file(file_path)
    totals = {}

    for defect in defects:
        status = (defect.get("Status") or "").strip()

        if status:
            totals[status] = totals.get(status, 0) + 1

    return totals

# python -m pytest -s test_execution_metrics.py

from execution_metrics import (
    calculate_execution_totals,
    calculate_defect_totals,
    EXECUTION_FILE,
    DEFECT_FILE,
)


def test_execution_totals():
    """Read the execution CSV and display execution totals."""

    totals = calculate_execution_totals(EXECUTION_FILE)

    total = sum(totals.values())

    print()
    print("========================================")
    print("       TEST EXECUTION RESULTS")
    print("========================================")
    print(f"Pass:        {totals['pass']}")
    print(f"Fail:        {totals['fail']}")
    print(f"Blocked:     {totals['blocked']}")
    print(f"Not Started: {totals['not_started']}")
    print("----------------------------------------")
    print(f"Total:       {total}")
    print("========================================")

    # Verify that we actually found executions
    assert total > 0


def test_defect_totals():
    """Read the defect CSV and display defect totals."""

    totals = calculate_defect_totals(DEFECT_FILE)

    total = sum(totals.values())

    print()
    print("========================================")
    print("            DEFECT RESULTS")
    print("========================================")

    for status, count in sorted(totals.items()):
        print(f"{status:<15} {count}")

    print("----------------------------------------")
    print(f"Total:           {total}")
    print("========================================")

    # Verify that we actually found defects
    assert total > 0

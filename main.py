"""Command line entry point for automation tasks."""

import argparse
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Automation scripts")
    sub = parser.add_subparsers(dest="command", required=True)

    inv = sub.add_parser("invoice", help="Create invoices")
    inv.add_argument("tasks", type=int, help="Number of invoices to create")

    pay = sub.add_parser("payment", help="Record payments")
    pay.add_argument("tasks", type=int, help="Number of payments to record")
    pay.add_argument("date", help="Payment received date (YYYY-MM-DD)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "invoice":
        from invoices_data_entry import main as invoice_main
        invoice_main(args.tasks)
    elif args.command == "payment":
        subprocess.run([sys.executable, "record_payment.py", str(args.tasks), args.date], check=False)


if __name__ == "__main__":
    main()

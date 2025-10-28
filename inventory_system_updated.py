import json
from datetime import datetime
from typing import Dict, List


# Global variable
stock_data: Dict[str, int] = {}


def add_item(item: str = "default", qty: int = 0, logs: List[str] | None = None) -> None:
    """Add an item and its quantity to the stock."""
    if not item or not isinstance(item, str) or not isinstance(qty, int):
        return

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    """Remove quantity of an item from the stock."""
    if not isinstance(item, str) or not isinstance(qty, int):
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not found
        pass


def get_qty(item: str) -> int:
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path: str = "inventory.json") -> None:
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
    except FileNotFoundError:
        stock_data = {}
    except json.JSONDecodeError:
        stock_data = {}


def save_data(file_path: str = "inventory.json") -> None:
    """Save inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data() -> None:
    """Print all items and their quantities."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> list[str]:
    """Return a list of items below the specified stock threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Main function to test inventory operations."""
    logs: list[str] = []

    add_item("apple", 10, logs)
    add_item("banana", 2, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()

    # Print logs
    print("\nActivity Log:")
    for log_entry in logs:
        print(log_entry)


if __name__ == "__main__":
    main()
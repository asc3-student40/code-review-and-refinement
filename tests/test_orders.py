import sys
import os
import pytest

# Ensure project root is in sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inventory import Inventory
from orders import inv, process_order


def setup_function():
    inv.items = []


def test_process_order_returns_formatted_price():
    inv.add_item("widget", 10)
    result = process_order("widget", 2)
    assert isinstance(result, str)
    assert result.startswith("$")


def test_process_order_insufficient_stock_returns_none():
    inv.add_item("gadget", 1)
    result = process_order("gadget", 5)
    assert result is None


def test_inventory_add_and_get():
    local = Inventory()
    local.add_item("thing", 3)
    assert local.get_stock("thing") == 3


def test_process_order_handles_missing_item():
    # No item added to inventory

    result = process_order("nonexistent", 1)

    # Expected behavior: should not crash and should return None
    assert result is None


def test_process_order_invalid_inputs():
    inv.add_item("item", 10)

    # negative quantity
    assert process_order("item", -1) is None

    # invalid coupon
    assert process_order("item", 2, 150) is None

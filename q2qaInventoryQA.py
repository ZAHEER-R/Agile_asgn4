import pytest
from InventoryManagement import InventoryManagement

def test_stock_availability_and_fulfillment():
    inv = InventoryManagement()
    inv.add_product("Warehouse A", "P1", 100, 10, "SupplierX")
    wh = inv.fulfill_order("P1", 20)
    assert wh == "Warehouse A"

def test_insufficient_inventory():
    inv = InventoryManagement()
    inv.add_product("Warehouse A", "P1", 5, 2, "SupplierX")
    with pytest.raises(ValueError, match="Insufficient inventory"):
        inv.fulfill_order("P1", 10)

def test_negative_inventory():
    inv = InventoryManagement()
    with pytest.raises(ValueError, match="Negative inventory"):
        inv.add_product("Warehouse B", "P2", -10, 5, "SupplierY")

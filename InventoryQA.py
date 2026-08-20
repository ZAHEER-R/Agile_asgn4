from InventoryManagement import InventorySystem

def run_tests():
    print("--- RUNNING INVENTORY QA TESTS ---")
    inv = InventorySystem()
    inv.add_product("Warehouse A", "P1", 20)
    inv.add_product("Warehouse B", "P1", 50)

    # 1. Stock Availability & Auto Selection
    best = inv.select_best_warehouse("P1", 30)
    print(f"[Test 1 Auto Warehouse Selection] Selected: {best} (Expected: Warehouse B)")

    # 2. Insufficient Inventory
    res, msg = inv.remove_product("Warehouse A", "P1", 100)
    print(f"[Test 2 Insufficient Stock] Success: {res} | Output: {msg}")

    # 3. Warehouse Transfer
    res, msg = inv.transfer_stock("Warehouse B", "Warehouse C", "P1", 15)
    print(f"[Test 3 Stock Transfer] Success: {res} | Output: {msg}")

    # 4. Reorder Threshold Trigger
    res, msg = inv.remove_product("Warehouse A", "P1", 12) # remaining 8 <= 10
    print(f"[Test 4 Reorder Threshold] Output: {msg}")

    # 5. Invalid Product
    res, msg = inv.remove_product("Warehouse A", "INVALID_ITEM", 1)
    print(f"[Test 5 Invalid Product] Success: {res} | Output: {msg}")

    # 6. Negative Inventory Input
    res, msg = inv.add_product("Warehouse A", "P2", -5)
    print(f"[Test 6 Negative Inventory] Success: {res} | Output: {msg}")

if __name__ == "__main__":
    run_tests()

class InventorySystem:
    def __init__(self):
        self.warehouses = {
            "Warehouse A": {"location": (0, 0), "stock": {}},
            "Warehouse B": {"location": (10, 20), "stock": {}},
            "Warehouse C": {"location": (50, 50), "stock": {}}
        }
        self.reorder_thresholds = {}

    def add_product(self, warehouse, product_id, quantity, reorder_level=10):
        if warehouse not in self.warehouses:
            return False, "Invalid Warehouse."
        if quantity < 0:
            return False, "Cannot add negative inventory."
        
        stock = self.warehouses[warehouse]["stock"]
        stock[product_id] = stock.get(product_id, 0) + quantity
        self.reorder_thresholds[product_id] = reorder_level
        return True, f"Added {quantity} of {product_id} to {warehouse}."

    def remove_product(self, warehouse, product_id, quantity):
        if warehouse not in self.warehouses:
            return False, "Invalid Warehouse."
        stock = self.warehouses[warehouse]["stock"]
        if product_id not in stock or stock[product_id] < quantity:
            return False, "Insufficient stock or invalid product."
        
        stock[product_id] -= quantity
        status = f"Removed {quantity} of {product_id} from {warehouse}."
        if stock[product_id] <= self.reorder_thresholds.get(product_id, 10):
            status += " [LOW STOCK ALERT]"
        return True, status

    def transfer_stock(self, source, target, product_id, quantity):
        if source not in self.warehouses or target not in self.warehouses:
            return False, "Invalid warehouse selection."
        success, msg = self.remove_product(source, product_id, quantity)
        if not success:
            return False, f"Transfer Failed: {msg}"
        self.add_product(target, product_id, quantity)
        return True, f"Transferred {quantity} units of {product_id} from {source} to {target}."

    def select_best_warehouse(self, product_id, quantity):
        for wh_name, wh_data in self.warehouses.items():
            if wh_data["stock"].get(product_id, 0) >= quantity:
                return wh_name
        return None

if __name__ == "__main__":
    inv = InventorySystem()
    inv.add_product("Warehouse A", "P100", 50)
    print(inv.select_best_warehouse("P100", 20))

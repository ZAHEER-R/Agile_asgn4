class InventoryManagement:
    def __init__(self):
        # Warehouses: A, B, C storing product inventory {product_id: {'stock': int, 'threshold': int, 'supplier': str}}
        self.warehouses = {
            "Warehouse A": {},
            "Warehouse B": {},
            "Warehouse C": {}
        }

    def add_product(self, warehouse, product_id, stock, threshold, supplier):
        if warehouse not in self.warehouses:
            raise ValueError("Invalid warehouse selection.")
        if stock < 0:
            raise ValueError("Negative inventory not allowed.")
        self.warehouses[warehouse][product_id] = {
            'stock': stock,
            'threshold': threshold,
            'supplier': supplier
        }

    def remove_product(self, warehouse, product_id):
        if product_id in self.warehouses[warehouse]:
            del self.warehouses[warehouse][product_id]
        else:
            raise ValueError("Invalid product.")

    def transfer_stock(self, from_wh, to_wh, product_id, qty):
        if product_id not in self.warehouses[from_wh] or self.warehouses[from_wh][product_id]['stock'] < qty:
            raise ValueError("Insufficient inventory for transfer.")
        self.warehouses[from_wh][product_id]['stock'] -= qty
        if product_id not in self.warehouses[to_wh]:
            self.warehouses[to_wh][product_id] = self.warehouses[from_wh][product_id].copy()
            self.warehouses[to_wh][product_id]['stock'] = qty
        else:
            self.warehouses[to_wh][product_id]['stock'] += qty

    def fulfill_order(self, product_id, required_qty):
        # Automatically identify best warehouse (highest stock or available)
        best_wh = None
        max_stock = -1
        for wh, inventory in self.warehouses.items():
            if product_id in inventory and inventory[product_id]['stock'] >= required_qty:
                if inventory[product_id]['stock'] > max_stock:
                    max_stock = inventory[product_id]['stock']
                    best_wh = wh
        if not best_wh:
            raise ValueError("Insufficient inventory across all warehouses.")
        self.warehouses[best_wh][product_id]['stock'] -= required_qty
        return best_wh

    def check_low_stock(self):
        low_stock_alerts = []
        for wh, inventory in self.warehouses.items():
            for prod, data in inventory.items():
                if data['stock'] <= data['threshold']:
                    low_stock_alerts.append((wh, prod))
        return low_stock_alerts

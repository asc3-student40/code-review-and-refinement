class Inventory:
    def __init__(self, items=[]):
        self.items = items

    def add_item(self, name, qty):
        self.items.append({"name": name, "qty": qty})

    def get_stock(self, name):
        for item in self.items:
            if item["name"] == name:
                return item["qty"]
        return None

    def updateStock(self, name, qty):
        for item in self.items:
            if item["name"] == name:
                item["qty"] = qty
                return True
        return False

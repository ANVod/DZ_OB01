class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        """Добавляет товар в ассортимент"""
        self.items[name] = price

    def remove_item(self, name):
        """Удаляет товар из ассортимента"""
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        """Возвращает цену товара по его названию"""
        return self.items.get(name)

    def update_price(self, name, price):
        """Обновляет цену товара"""
        if name in self.items:
            self.items[name] = price



store1 = Store("Магнолия", "ул. Пушкина, 23")
store2 = Store("Лотос", "пр. Ленина, 12")
store3 = Store("Орхидея", "ул. Солнечная, 5")

store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("макароны", 1.5)
store2.add_item("рис", 2.0)

store3.add_item("чай", 3.5)
store3.add_item("кофе", 5.75)

print("Цена яблок:", store1.get_price("яблоки"))
store1.update_price("яблоки", 0.55)
print("Новая цена яблок:", store1.get_price("яблоки"))

store1.remove_item("бананы")
print("Цена бананов после удаления:", store1.get_price("бананы"))
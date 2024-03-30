class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        return self.items.get(name, None)

    def update_price(self, name, price):
        if name in self.items:
            self.items[name] = price



# Создание магазинов и управление товарами
store1 = Store("Магнолия", "ул. Пушкина, д.23")
store2 = Store("Огонёк", "пр. Мира, д.12")
store3 = Store("Лукоморье", "ул. Строителей, д.5")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("milk", 1.0)
store3.add_item("bread", 1.2)
store3.add_item("butter", 2.5)

# Тестирование методов на примере store1
print("Цена яблок до обновления:", store1.get_price("apples"))
store1.update_price("apples", 0.6)
print("Цена яблок после обновления:", store1.get_price("apples"))

store1.add_item("oranges", 0.8)
print("Цена добавленных апельсинов:", store1.get_price("oranges"))

store1.remove_item("bananas")
print("Цена бананов после их удаления:", store1.get_price("bananas"))

# Вывод всех текущих товаров магазина store1
print("Текущий ассортимент магазина", store1.name, ":")
for item, price in store1.items.items():
    print(item, ":", price)
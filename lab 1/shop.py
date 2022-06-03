class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self, type, service):
        return f"Магазин продає {type}, а також займається {service}"

    def open_shop(self):
        return f"Онлайн-магазин {self.shop_name} відкритий"

    def number_of_units(self):
        return f"Кількість видів товару в магазині: {self.number_of_units}"

    def increment_number_of_units(self, number):
        return f"Кількість видів товару в магазині: {self.number_of_units + number}"
    pass


store = Shop("Sport", "спортивні товари")
print(store.describe_shop("спортивні товари", "послугами"))
print(store.open_shop())

store = Shop("Products", "продукти")
print(store.describe_shop("харчові продукти", "доставкою"))
print(store.open_shop())

store = Shop("Wardrobe", "одяг")
print(store.describe_shop("різноманітний одяг", "доставкою"))
print(store.open_shop())

print(store.increment_number_of_units(26))


class Discount(Shop):
    def __init__(self, discount_products):
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        return f"Сьогоднішні товари по знижці: {self.discount_products}"
    pass


store_discount = Discount(["волейбольний м'яч", "ракетки"])

print(store_discount.get_discounts_ptoducts())
from abc import ABC, abstractmethod

# Packing Interface for tablets
class Packing(ABC):
    @abstractmethod
    def pack(self):
        pass

    @abstractmethod
    def price(self):
        pass

# Tablet abstract class implementing Packing
class Tablet(Packing):
    @abstractmethod
    def pack(self):
        pass

# Company abstract class extending Tablet
class Company(Tablet):
    @abstractmethod
    def price(self):
        pass

# Concrete Lenovo class
class Lenovo(Company):
    def price(self):
        return 600

    def pack(self):
        return "Lenovo Yoga"

# Concrete MicroMax class
class MicroMax(Company):
    def price(self):
        return 400

    def pack(self):
        return "MicroMax"

# TabType class to represent a complex tablet order
class TabType:
    def __init__(self):
        self.items = []

    # Add items to the order
    def add_item(self, item):
        self.items.append(item)

    # Retrieve total cost
    def get_cost(self):
        return sum(item.price() for item in self.items)

    # Show all items in the order
    def show_items(self):
        for item in self.items:
            print(f"Tablet name: {item.pack()}, Price (USD): {item.price()}")

# Builder class for tablet orders
class TabBuilder:
    # Build Lenovo tab
    def build_lenovo_tab(self):
        lenovo_order = TabType()
        lenovo_order.add_item(Lenovo())
        return lenovo_order

    # Build MicroMax tab
    def build_micromax_tab(self):
        micromax_order = TabType()
        micromax_order.add_item(MicroMax())
        return micromax_order

# Main code to demonstrate the Builder Pattern
if __name__ == "__main__":
    # Create a TabBuilder object
    tab_builder = TabBuilder()

    # Build Lenovo order and show details
    lenovo_tab = tab_builder.build_lenovo_tab()
    print("Lenovo Tablet Order:")
    lenovo_tab.show_items()

    # Build MicroMax order and show details
    micromax_tab = tab_builder.build_micromax_tab()
    print("\nMicroMax Tablet Order:")
    micromax_tab.show_items()
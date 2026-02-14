"""
Composite Pattern Implementation
Manages hierarchical inventory structure.
"""

from abc import ABC, abstractmethod
from typing import List


class InventoryComponent(ABC):

    @abstractmethod
    def show_details(self) -> None:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass


class Product(InventoryComponent):

    def __init__(self, name: str, price: float, sku_id: int):
        self.name = name
        self.price = price
        self.sku_id = sku_id

    def show_details(self) -> None:
        print(f" - Product: {self.name} [ID: {self.sku_id}] (${self.price})")

    def get_price(self) -> float:
        return self.price


class Category(InventoryComponent):

    def __init__(self, name: str):
        self.name = name
        self._children: List[InventoryComponent] = []

    def add(self, component: InventoryComponent) -> None:
        self._children.append(component)

    def remove(self, component: InventoryComponent) -> None:
        self._children.remove(component)

    def show_details(self) -> None:
        print(f"Category: {self.name}")
        for child in self._children:
            child.show_details()

    def get_price(self) -> float:
        total = 0.0
        for child in self._children:
            total += child.get_price()
        return total

    def find_product(self, sku_id: int):
        for child in self._children:
            if isinstance(child, Product) and child.sku_id == sku_id:
                return child
            elif isinstance(child, Category):
                found = child.find_product(sku_id)
                if found:
                    return found
        return None

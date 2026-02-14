"""
Logistics Module
Implements Observer Pattern + Queue Management using deque
"""

from collections import deque, namedtuple
from typing import Optional


Order = namedtuple('Order', ['id', 'customer', 'destination', 'priority'])


class OrderSubject:

    def __init__(self):
        self._observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class CustomerObserver:

    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f" >> [Notification to {self.name}]: {message}")


class OrderQueueManager(OrderSubject):

    def __init__(self):
        super().__init__()
        self.queue: deque[Order] = deque()      
        self.completed_stack: deque[Order] = deque()  

    def add_order(self, order: Order) -> None:
        """
        Adds order to queue.
        VIP priority (priority == 0) goes to front.
        """

        if order.priority == 0:
            self.queue.appendleft(order)  
        else:
            self.queue.append(order)      

        print(f"[Queue] Order #{order.id} added for {order.customer}.")
        self.notify(f"Order #{order.id} is now PENDING.")

    def process_next(self) -> Optional[Order]:
        """
        Processes next order in FIFO order.
        """

        if not self.queue:
            print("[Queue] No orders to process.")
            return None

        order = self.queue.popleft()   

        print(f"[Queue] Processing Order #{order.id}...")
        self.notify(f"Order #{order.id} is now SHIPPED.")

        self.completed_stack.append(order)

        return order   

    def undo_last_completed(self) -> Optional[Order]:
        """
        Pops last completed order (Stack behavior).
        """

        if not self.completed_stack:
            print("[History] No completed orders.")
            return None

        order = self.completed_stack.pop()
        print(f"[History] Undo Order #{order.id}")
        return order

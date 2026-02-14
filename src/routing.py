"""
Routing Module
Implements Strategy Pattern + Facade Pattern using NetworkX
"""

import csv
import networkx as nx
from abc import ABC, abstractmethod


class RoutingStrategy(ABC):

    @abstractmethod
    def calculate_route(self, graph: nx.Graph, start: str, end: str):
        pass


class FastestRouteStrategy(RoutingStrategy):

    def calculate_route(self, graph: nx.Graph, start: str, end: str):
        print(f"[Strategy] Calculating fastest route from {start} to {end}...")

        try:
            return nx.shortest_path(
                graph,
                source=start,
                target=end,
                weight="weight"   
            )
        except nx.NetworkXNoPath:
            print("Error: No path found.")
            return None


class CheapestRouteStrategy(RoutingStrategy):

    def calculate_route(self, graph: nx.Graph, start: str, end: str):
        print(f"[Strategy] Calculating cheapest route from {start} to {end}...")

        try:
            return nx.shortest_path(graph, source=start, target=end)
        except nx.NetworkXNoPath:
            print("Error: No path found.")
            return None


class CityMapFacade:

    def __init__(self, strategy: RoutingStrategy):
        self.graph = nx.Graph()
        self.strategy = strategy

    def load_map_from_csv(self, file_path: str) -> None:
        """
        Reads CSV file and builds weighted graph.
        Expected columns:
        source,destination,distance_km
        """

        print(f"[Map] Loading data from {file_path}...")

        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                source = row["source"]
                destination = row["destination"]
                distance = float(row["distance_km"])

                self.graph.add_edge(source, destination, weight=distance)

        print("[Map] Graph loaded successfully.")

    def get_route(self, start: str, end: str):
        return self.strategy.calculate_route(self.graph, start, end)

    def set_strategy(self, strategy: RoutingStrategy):
        """
        Allows switching routing strategy at runtime.
        """
        self.strategy = strategy



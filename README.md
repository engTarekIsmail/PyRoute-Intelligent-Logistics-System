PyRoute – Intelligent Logistics Optimization System

PyRoute is a Python-based logistics simulation system designed to optimize delivery operations in a city network. The system demonstrates core software design patterns and provides a modular architecture for managing inventory, processing orders, and calculating delivery routes.

Features

Inventory Management: Organize products into categories, view inventory details, and manage stock items.

Order Queue System: Add, process, and track orders efficiently using an observer-based notification system.

Routing Engine: Calculate the fastest route between locations using a pluggable strategy pattern.

Interactive CLI: User-friendly command-line interface for performing all operations.

Design Patterns Showcase: Implements Singleton, Observer, Strategy, and Builder patterns to demonstrate best practices in software design.

How It Works

Inventory Setup – Products are categorized, and mock data can be loaded or replaced with file I/O.

Order Processing – Users can add orders for customers and process them in queue order.

Routing – Calculates the optimal path between start and destination nodes in the city network.

Notifications – Customers are notified when their orders are processed via an Observer pattern implementation.

Technologies Used

Python 3.14.2

Object-Oriented Programming (OOP)

NetworkX (optional, for graph-based routing)

Design Patterns (Singleton, Observer, Strategy, Builder)


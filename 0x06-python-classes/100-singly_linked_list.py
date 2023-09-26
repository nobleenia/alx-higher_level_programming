#!/usr/bin/python3
"""
Node Class
Defines a node of a singly linked list
"""

class Node:
    """
    This class represents a node in a singly linked list.

    Attributes:
    - data (int): The data stored in the node.
    - next_node (Node): Reference to the next node in the list, or None if it's the last node.

    Methods:
    - __init__(self, data, next_node=None): Initializes a new node with the specified data.
        - data (int): The data to be stored in the node.
        - next_node (Node): Reference to the next node in the list (default is None).
        - Raises:
            - TypeError: If data is not an integer.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node with the specified data.

        Args:
        - data (int): The data to be stored in the node.
        - next_node (Node): Reference to the next node in the list (default is None).

        Raises:
        - TypeError: If data is not an integer.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
        - int: The data in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node to a new value.

        Args:
        - value (int): The new data to be stored in the node.

        Raises:
        - TypeError: If value is not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node in the list.

        Returns:
        - Node or None: Reference to the next node in the list, or None if it's the last node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node in the list.

        Args:
        - value (Node or None): Reference to the next node in the list, or None if it's the last node.

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Convert the linked list into a string representation.

        Returns:
        - str: A string representation of the linked list where each element is separated by a newline character.
        """
        string = ""
        temp_node = self.__head

        while temp_node is not None:
            string += str(temp_node.data)
            temp_node = temp_node.next_node
            if temp_node is not None:
                string += "\n"
        return string
    
    def sorted_insert(self, value):
        """
        Insert a new node with the specified value into the sorted position of the linked list.

        Args:
        - value (int): The value to be inserted into the linked list.

        Description:
        This method inserts a new node with the specified value into the linked list while maintaining
        ascending order based on the values of the nodes. If the list is initially empty, the new node
        becomes the head of the list.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            while temp_node.next_node is not None and temp_node.next_node.data < value:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

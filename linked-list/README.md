# Singly Linked List

Linked List can be defined as a data structure that containes of nodes that connected or points to each other.

A node contains two fields i.e. data stored at that particular address and the pointer which contains the address of the next node in the memory.

## Challenge

Within the LinkedList class, include method to axcess the property of head value to check if the value in linked list or not. And, Upon instantiation, an empty Linked List should be created.

## Approach & Efficiency

First create a class for creating a node to store a value, and a pointer to the next node. Then create a  class for creating instances of a Linked List inside this class define three methode. first one is insert to create a Node with the value that was passed and adds it to the head of the linked list shifting all other values down, second one is include to return True or False if value is in the linked list or not and third one str method that returns a string representing all the values in the Linked List.

## API

`insert`: to create a Node with the value that was passed and adds it to the head of the linked list shifting all other values down.

- time : O(1)
- space : O(1)

`includes`: to check if the value in the linked lis or not then returns True or False if value is in the linked list or not.

- time : O(n)
- space : O(1)

`__str__`: to return a string representing all the values in the Linked List.

- time : O(n)
- space : O(n)

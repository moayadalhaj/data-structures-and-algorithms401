from linked_list import __version__
import linked_list
from linked_list.linked_list import Linked_list, Node

def test_version():
    assert __version__ == '0.1.0'

def test_Node():
    # Arrange any data that you need to run your test
    expected1=5
    expected2=3
    # Act on the subject of the test to produce some actual output
    a = Node(5,3)
    # Assert
    assert a.value == expected1
    assert a.next == expected2

def test_empety_linked_list():
    # Arrange any data that you need to run your test
    expected=None
    # Act on the subject of the test to produce some actual output
    a = Linked_list()
    # Assert
    assert a.head == expected

def test_the_head_value():
    # Arrange any data that you need to run your test
    expected=5
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    ll.insert(7)
    actual=ll.head.value
    # Assert
    assert actual == expected

def test_insert_multiple_nodes():
    # Arrange any data that you need to run your test
    expected='{ 5 } -> { 8 } -> None'
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    ll.insert(8)
    actual=str(ll)
    # Assert
    assert actual == expected

def test_insert():
    # Arrange any data that you need to run your test
    expected1=5
    expected2=None
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    actual1=ll.head.value
    actual2=ll.head.next
    # Assert
    assert actual1 == expected1
    assert  actual2 == expected2

def test_value_include_in_linjed_list():
    # Arrange any data that you need to run your test
    excepted=True
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(5)
    actual=ll.includes(5)
    # Assert
    assert actual == excepted

def test_value_doesnt_include_in_linked_list():
    # Arrange any data that you need to run your test
    excepted=False
    # Act on the subject of the test to produce some actual output
    ll = Linked_list()
    ll.insert(3)
    actual=ll.includes(7)
    # Assert
    assert actual == excepted

def test_str():
    # Arrange any data that you need to run your test
    excpected='{ 5 } -> { s } -> { 17 } -> None'
    # Act on the subject of the test to produce some actual output
    ll=Linked_list()
    ll.insert(5)
    ll.insert('s')
    ll.insert(17)
    # Assert
    assert str(ll) == excpected

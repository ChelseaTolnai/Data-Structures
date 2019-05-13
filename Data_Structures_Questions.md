Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
- O(1)

2. What is the runtime complexity of `dequeue`?
- O(1)

3. What is the runtime complexity of `len`?
- O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
- O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
- O(1)

3. What is the runtime complexity of `ListNode.delete`?
- O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
- O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
- O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
- O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
- O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
- O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
- O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
- O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    - Doubly linked lists delete method has a runtime of O(1) which generally will perform better than the Array.splice method which at worst case has a runtime of O(n). Splice has this worst case runtime becuase it essentially makes a copy of all elements of the Array from the zeroth elementh to (n-1) into a new Array. If n lies near or at the end of the array it runs towards to O(n) time.
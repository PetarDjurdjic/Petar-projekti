from Linked_List_Class import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1



customLL=LinkedList()
customLL.generate(10,0,90)
print(customLL)
print(nthToLast(customLL,2))

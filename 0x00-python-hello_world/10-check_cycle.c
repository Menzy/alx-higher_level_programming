#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @head: pointer to the head of the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
    listint_t *slow_ptr;
    listint_t *fast_ptr;

    if (head == NULL)
        return 0; // No cycle in an empty list

    slow_ptr = head;
    fast_ptr = head;

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        if (slow_ptr == fast_ptr)
            return 1; // Cycle detected
    }

    return 0; // No cycle found
}

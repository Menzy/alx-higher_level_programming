#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted linked list.
 * @head: The head of the linked list.
 * @number: Data in the new node.
 * Return: Address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode, *current, *prev;

    newnode = malloc(sizeof(listint_t));
    if (newnode == NULL)
        return (NULL);

    newnode->n = number;
    newnode->next = NULL;

    current = *head;
    prev = NULL;

    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL)
    {
        newnode->next = *head;
        *head = newnode;
    }
    else
    {
        newnode->next = current;
        prev->next = newnode;
    }

    return (newnode);
}

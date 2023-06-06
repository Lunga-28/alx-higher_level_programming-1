#include <stdlib.h>

/**
 * create_node - Creates a new node with the given number
 * @number: The number to be stored in the node
 *
 * Return: The address of the new node, or NULL if memory allocation failed
 */
listint_t *create_node(int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));

    if (new_node)
    {
        new_node->n = number;
        new_node->next = NULL;
    }

    return new_node;
}

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: A pointer to the pointer to the head of the linked list
 * @number: The number to be inserted
 *
 * Return: The address of the new node, or NULL if memory allocation failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = create_node(number);
    listint_t *current = *head, *prev = NULL;

    if (!new_node)
        return NULL;

    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (!prev)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        prev->next = new_node;
        new_node->next = current;
    }

    return new_node;
}

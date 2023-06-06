#include <stdio.h>
#include <stdlib.h>

/**
 * create_node - Creates a new node with the given number
 * @number: The number to be stored in the node
 *
 * Return: The address of the new node, or NULL if memory allocation failed
 */


/* Definition of a singly linked list node */
typedef struct listint_s {
    int data;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  // Memory allocation failed
    }
    new_node->data = number;

    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
    } else {
        listint_t *current = *head;
        while (current->next != NULL && current->next->data < number) {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}


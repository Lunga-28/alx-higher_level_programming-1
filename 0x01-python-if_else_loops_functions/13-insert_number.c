#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * create_node - Creates a new node with the given number
 * @number: The number to be stored in the node
 *
 * Return: The address of the new node, or NULL if memory allocation failed
 */


/* Definition of a singly linked list node */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tp;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
        
		return (newnode);
	}
	else 
        if (number <= (*head)->n)
	{
		newnode->n = number;
		newnode->next = *head;
        
		*head = newnode;
		return (newnode);
	}
	else
	{
		tp = *head;
        
		while (tp->next != NULL && number > tp->next->n)
		{
			tp = tp->next;
		}
		newnode->n = number;
		newnode->next = tp->next;
        
		tp->next = newnode;
        
		return (newnode);
	}
	return (NULL);
}

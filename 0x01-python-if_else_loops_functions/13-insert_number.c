#include <stdlib.h>
#include "lists.h"

/**
 * create_node - ...
 * @number: ...
 *
 * Return: ...
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tmp;

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
		tmp = *head;
        
		while (tmp->next != NULL && number > tmp->next->n)
		{
			tmp = tmp->next;
		}
		newnode->n = number;
		
		newnode->next = tmp->next;
        
		tmp->next = newnode;
        
		return (newnode);
	}
	return (NULL);
}

#include "lists.h"

/**
 * reverse_listint - ...
 * @head: Pointer ...
 *
 * Return: ...
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	
	listint_t *current = *head;
	
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		
		current->next = prev;
		
		prev = current;
		
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - ...
 * @head: ...
 *
 * Return: ...
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		
		if (!fast)
		{
			duplicate = slow->next;
			
			break;
		}
		if (!fast->next)
		{
			duplicate = slow->next->next;
			
			break;
		}
		slow = slow->next;
	}

reverse_listint(&duplicate);
	
while (duplicate && temp)
	{
		if (temp->n == duplicate->n)
		{
			duplicate = duplicate->next;
			
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!duplicate)
		
		return (1);

	return (0);
}

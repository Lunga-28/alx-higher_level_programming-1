#include "lists.h"

/**
 * reverse_listint - ...
 * @head: ...
 *
 * Return: ...
 */
void reverse_listint(listint_t **head)
{
	listint_t *prevs = NULL;
	listint_t *curr = *head;
	listint_t *nex = NULL;

	while (curr)
	{
		nex = curr->nex;
		curr->nex = prevs;
		prevs = curr;
		curr = nex;
	}
	*head = prevs;
}

/**
 * is_palindrome - ...
 * @head: ...
 *
 * Return: ...
 */
int is_palindrome(listint_t **head)
{
	listint_t *slo = *head, *fast = *head, *temp = *head, *dupli = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dupli = slo->next;
			break;
		}
		if (!fast->next)
		{
			dupli = slo->next->next;
			break;
		}
		slo = slow->next;
	}

	reverse_listint(&dupli);

	while (dupli && temp)
	{
		if (temp->n == dupli->n)
		{
			dupli = dupli->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dupli)
		return (1);

	return (0);
}

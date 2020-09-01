#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list)
		return (0);
	tortoise = list;
	if (!(tortoise->next))
		return (0);
	hare = tortoise->next;
	for (; tortoise; tortoise = tortoise->next)
	{
		if (tortoise == hare)
			return (1);
		else if (!hare)
			return (0);
		else if (!(hare->next))
			return (0);
		hare = hare->next->next;
	}
	return (0);
}

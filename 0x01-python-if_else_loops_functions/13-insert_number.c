#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: the int number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *actual, *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	for (actual = *head; actual; actual = actual->next)
	{
		if (!(actual->next)->next)
			break;
		if ((actual->next)->n > number)
			break;
	}
	if (!(actual->next)->next)
		actual = actual->next;
	new->n = number;
	if (actual == *head)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = actual->next;
		actual->next = new;
	}

	return (new);
}

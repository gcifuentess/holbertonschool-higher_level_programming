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
	listint_t *actual, *temp, *previous;

	if (!head)
		return (NULL);
	temp = malloc(sizeof(temp));
	if (!temp)
		return (NULL);
	previous = *head;
	for (actual = *head; actual; actual = actual->next)
	{
		if (actual->n > number)
			break;
		previous = actual;
	}
	temp->n = number;
	if (actual == *head)
	{
		temp->next = *head;
		*head = temp;
	}
	else
	{
		temp->next = previous->next;
		previous->next = temp;
	}

	return (temp);
}

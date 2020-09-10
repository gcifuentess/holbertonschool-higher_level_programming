#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - verifyes is a linked list is  a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *single_j, *double_j, *prev, *current, *next;
	int palindrome = 1;

	if (!(*head) || !((*head)->next))
		return (palindrome);

	for (single_j = *head, double_j = *head; double_j && double_j->next; )
	{
		single_j = single_j->next;
		double_j = double_j->next->next;
	}
	for (current = single_j, prev = NULL; current; )
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	for (single_j = prev, current = *head; current->next; )
	{
		if (single_j->n == current->n)
			palindrome = 1;
		else
			palindrome = 0;
		single_j = single_j->next;
		current = current->next;
	}
	for (current = prev, prev = NULL; current != single_j; )
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (palindrome);
}

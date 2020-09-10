#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	clock_t start;
	clock_t end;
	clock_t diff;
	int i;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	printf("%p\n", (void *)head);
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	add_nodeint_end(&head, 1);
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	printf("\n====Eficency Test (1) ====\n");

	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint_end(&head, i);
	for (i = 1000; i >= 0; i--)
		add_nodeint_end(&head, i);

	start = clock();

	for (i = 0; i < 10; i++)
		is_palindrome(&head);

	end = clock();

	diff = (double)(end - start) / 10;

	if (diff > 80)
		printf("Runtime too long\n");
	else
		printf("OK\n");

	free_listint(head);

	printf("\n====Eficency Test (2) ====\n");
	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint_end(&head, i);
	for (i = 1000; i >= 0; i--)
		add_nodeint_end(&head, i);

	current = head;
	for (i = 0; i < 727; i++)
		current = current->next;
	current->n = -98;

	start = clock();

	for (i = 0; i < 10; i++)
		is_palindrome(&head);

	end = clock();

	diff = (double)(end - start) / 10;

	if (diff > 80)
		printf("Runtime too long\n");
	else
		printf("OK\n");

	free_listint(head);


	return (0);
}

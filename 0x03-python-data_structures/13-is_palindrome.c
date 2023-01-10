#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome -  a () in C that checks if a singly linked list
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int nodes = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		nodes++;
		temp = temp->next;
	}
	array = malloc(sizeof(int) * nodes);
	temp = *head;
	while (temp)
	{
		array[i++] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (array[i] != array[nodes - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}

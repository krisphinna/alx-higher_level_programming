#include "lists.h"

/**
 * check_cycle - to checks if a singly linked list has a cycle in it
 * @list: the list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s1 = NULL, *s2 = NULL;

	s1 = s2 = list;
	while (list && s1 && s2 && s1->next && s2->next)
	{
		s1 = s1->next;
		s2 = s2->next->next;
		if (!s2 || !s1)
			return (0);
		if (s2->next == s1)
			return (1);
	}
	return (0);
}

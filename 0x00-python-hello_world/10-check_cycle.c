#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 is there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
listint_t *first;
listint_t *last;

if (list == NULL)
{
return (0);
}

first = list;
last = list;

while (first != NULL && last != NULL && last->next != NULL)
{
first = first->next;
last = last->next->next;

if (first == last)
{
return (1);
}
}
return (0);
}

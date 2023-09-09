#include "lists.h"

/**
 * len - find size of a list
 * @ls: list
 * Return: length of the list
 */

unsigned int len(listint_t *list)
{
unsigned int length = 0;

while (list)
{
length++;
list = list->next;
}
return (length);
}

/**
 * is_palindrome - check if a list is a palindrome
 * @head: first node in the linked list
 *
 * Return: yes ? 1 : 0
 */
int is_palindrome(listint_t **head)
{
listint_t *temp = *head;
unsigned int size;
unsigned int i;
int data[10240];

if (!head)
{
return (0);
}
if (!*head)
{
return (1);
}

size = len(temp);

if (size == 1)
{
return (1);
}

i = 0;
while (temp)
{
data[i] = temp->n;
i++;
temp = temp->next;
}

for (i = 0; i <= size / 2; i++)
{
if (data[i] != data[size - i - 1])
{
return (0);
}
}

return (1);
}

#include "lists.h"

/**
 * *insert_node - inserts a number in a sorted singly linked list
 * @head: pointer to first node in the linked list
 * @number: position to insert node
 * Return: address of new node, NULL upon failure
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *temp;

new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
if (*head == NULL)
{
new->n = number;
new->next = *head;
*head = new;
return (new);
}
else if (number <= (*head)->n)
{
new->n = number;
new->next = *head;
*head = new;
return (new);
}
else
{
temp = *head;
while (temp->next != NULL && number > temp->next->n)
{
temp = temp->next;
}
new->n = number;
new->next = temp->next;
temp->next = new;
return (new);
}
return (NULL);
}

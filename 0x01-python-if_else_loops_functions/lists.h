fndef LISTS_H
#define LISTS_H

/* Structure for a singly-linked list node */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint(listint_t **head, int n);
void free_listint(listint_t *head);
void print_listint(const listint_t *h);
size_t listint_len(const listint_t *h);
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);
int pop_listint(listint_t **head);
listint_t *reverse_listint(listint_t **head);
int sum_listint(listint_t *head);
listint_t *find_listint_loop(listint_t *head);

#endif /* LISTS_H */

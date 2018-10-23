#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *left, *right;
};

struct node* insertion()
{
    struct node *newnode;
    int key;
    newnode=(struct node*) malloc( sizeof(struct node));
    printf("Enter the data(-1 for NULL):");
    scanf("%d",&key);
    if(key==-1)
        return NULL;
    newnode->data=key;
    printf("LEFT child of %d:\t",newnode->data);
    newnode->left=insertion();
    printf("RIGHT child of %d\t",newnode->data);
    newnode->right=insertion();
    return newnode;
}

void inorder(struct node *temp)
{
    if(temp==NULL)
        return;
    inorder(temp->left);
    printf("%d\t",temp->data);
    inorder(temp->right);
}

void preorder(struct node *temp)
{
    if(temp==NULL)
        return;
    printf("%d\t",temp->data);
    preorder(temp->left);
    preorder(temp->right);
}

void postorder(struct node *temp)
{
    if(temp==NULL)
        return;
    postorder(temp->left);
    postorder(temp->right);
    printf("%d\t",temp->data);
}

void main()
{
    struct node *root;
    root=insertion();
    printf("Inorder display:\n");
    inorder(root);
    printf("\nPreorder display:\n");
    preorder(root);
    printf("\nPostorder display:\n");
    postorder(root);
    printf("\n");
}
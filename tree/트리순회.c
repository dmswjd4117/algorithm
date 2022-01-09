#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#pragma warning(disable:6031)
#pragma warning(disable: 4996)

#define true 1
#define false 0


typedef char element;
typedef struct _treeNode TreeNode;

struct _treeNode {
    element data;
    TreeNode* left;
    TreeNode* right;
};

TreeNode* make_treeNode(TreeNode* left, TreeNode* right) {
    TreeNode* nNode = (TreeNode*)malloc(sizeof(TreeNode));
    nNode->left = left;
    nNode->right = right;
    return nNode;
}

 
void preorder(TreeNode* node) {
    if (node == NULL) {
        return;
    }

    printf("%c", node->data);
    preorder(node->left);
    preorder(node->right);
}

void inorder(TreeNode* node) {
    if (node == NULL) {
        return;
    }

    inorder(node->left);
    printf("%c", node->data);
    inorder(node->right);
}

void postoder(TreeNode* node) {
    if (node == NULL) {
        return;
    }

    postoder(node->left);
    postoder(node->right);
    printf("%c", node->data);
}


int ctoi(char a) {
    return a - 'A';
}

int main(void)
{
    TreeNode* nodes[30];
    for (int i = 0; i < 30; i++) {
        nodes[i] = make_treeNode(NULL, NULL);
        nodes[i]->data = 'A'+i;
    }
    int n;
    scanf("%d", &n);
    char a, b, c;

    for (int i = 0; i < n; i++) {
        scanf(" %c %c %c", &a, &b, &c);
        if (b != '.') {
            nodes[ctoi(a)]->left = nodes[ctoi(b)];
        }
        if (c != '.') {
            nodes[ctoi(a)]->right = nodes[ctoi(c)];
        }        
    }

    preorder(nodes[0]);
    printf("\n");

    inorder(nodes[0]);
    printf("\n");

    postoder(nodes[0]);
    printf("\n");

 
    return 0;
}

 
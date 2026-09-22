#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>
#include <stdlib.h>

#define TABLE_SIZE 100

typedef struct Node {
    int value;
    int count;
    struct Node* next;
} Node;

typedef struct {
    Node* buckets[TABLE_SIZE];
} HashMap;

unsigned int hash(int value) {
    return abs(value) % TABLE_SIZE;
}

void insertOrUpdate(HashMap* map, int value) {
    unsigned int index = hash(value);
    Node* current = map->buckets[index];
    while (current != NULL) {
        if (current->value == value) {
            current->count++;
            return;
        }
        current = current->next;
    }
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->value = value;
    newNode->count = 1;
    newNode->next = map->buckets[index];
    map->buckets[index] = newNode;
}

void printFrequencies(HashMap* map) {
    printf("\nTần suất xuất hiện của các phần tử:\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* current = map->buckets[i];
        while (current != NULL) {
            printf("Số %d xuất hiện %d lần\n", current->value, current->count);
            current = current->next;
        }
    }
}

void freeMap(HashMap* map) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        Node* current = map->buckets[i];
        while (current != NULL) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}

void count_number_with_hashmap(int arr[], int n) {
    HashMap map = { .buckets = { NULL } };

    // Thêm phần tử vào bảng băm
    for (int i = 0; i < n; i++) {
        insertOrUpdate(&map, arr[i]);
    }

    // In ra tần suất
    printFrequencies(&map);

    // Giải phóng bộ nhớ
    freeMap(&map);
}
void nhapmang(int arr[], int *n)
{
    printf("Nhap kich thuoc mang: ");
    scanf("%d", n);
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }
}
void inmang(int arr[], int *n)
{
    printf("In mang: ");
    for (int i = 0; i < *n; i++)
    {
        printf("arr[%d] = %d\t", i, arr[i]);
    }
    printf("\n");
}
void 
int main (){

}
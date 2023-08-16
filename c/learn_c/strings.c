#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct {
    string name;
    string number;

} human;

int main(void) {
    human people[2];
    people[0].name = "Joe Shmoe";
    people[0].number = "123";
    people[1].name = "Icy";
    people[1].number = "456";
    for (int j = 0; j < 2; j++) {
        if (strcmp(people[j].name, "David") == 0) {
            printf("Found\n");
        }
    }
};
// If length is unknown upfront
int main(void) {
    string names[] = {"Alex", "David"};
    int names_length = sizeof(names) / sizeof(names[0]);

    for (int i = 0; i < names_length; i++) {
        if (strcmp(names[i], "David") == 0) {
            printf("Found\n");
        }
    }

    return 0;
}
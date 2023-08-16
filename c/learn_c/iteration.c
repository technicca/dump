#include <stdio.h>
#include <cs50.h>
#include <string.h>

/* 1 implementation:
void draw(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            printf("#");
        }
        printf("\n");
    };
} 
*/

void draw (int n) {
    if (n <= 0) { return; }
    draw(n - 1); // Recursion
    for (int i = 0; i < n; i++) {
        printf("#");

    }
    printf("\n");
};

int main(void) {
    int height = get_int("Height:");
    draw(height);

};

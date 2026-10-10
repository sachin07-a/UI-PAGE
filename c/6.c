// taking input from user
#include <stdio.h>

int main() {
    int age;
    float pi;
    char star;

    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter the value of pi: ");
    scanf("%f", &pi);

    printf("Enter a star character: ");
    scanf(" %c", &star); // space before %c to consume any leftover newline character

    printf("You entered age: %d\n", age);
    printf("You entered value of pi: %.2f\n", pi);
    printf("You entered star character: %c\n", star);

    return 0;
}
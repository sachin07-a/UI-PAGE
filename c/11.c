#include <stdio.h>

int main() {
    int n;
    unsigned long long fact = 1;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Error: Factorial of a negative number does not exist.\n");
    } else {
        printf("%d! = ", n);

        for (int i = 1; i <= n; i++) {
            fact *= i;
            printf("%d", i);
            if (i < n) {
                printf(" * ");
            }
        }
        if (n == 0) {
            printf("1");
        }

        printf(" = %llu\n", fact);
    }

    return 0;
}

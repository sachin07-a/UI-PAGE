#include <stdio.h>

int main() {
    int n;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        int sum = 0;
        for (int j = 1; j <= i; j++) {
            sum += j;
            printf("%d", j);
            if (j < i) {
                printf("+");
            }
        }
        printf(" = %d\n", sum);
    }
// gcc aa.c -o aa.exe; .\aa.exe
    return 0;
}
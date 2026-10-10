#include <stdio.h>

int main() {
    long long n, res;
    int count = 0;
    int sum = 0;
    printf("Enter a number: ");
    scanf("%lld", &n);

    if (n < 0) {
        n = -n;
    }
    res= n;
    if (res == 0) {
        count = 1;
    }
    while (res != 0) {
        res /= 10;
        count++;
    }
    printf("Number of digits = %d\n", count);
    res = n;
    while (res != 0) {
        sum += res % 10;
        res /= 10;
    }

    printf("Sum of digits = %d\n", sum);

    return 0;
}

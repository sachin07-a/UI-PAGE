int main() {
    long long n, res;
    long long rev = 0;

    printf("Enter a number: ");
    scanf("%lld", &n);

    res = n;
    if (res < 0) {
        res = -res;
    }

    while (res != 0) {
        rev = rev * 10 + res % 10;
        res /= 10;
    }

    if (n < 0) {
        rev = -rev;
    }

    printf("Reversed number = %lld\n", rev);

    return 0;
}
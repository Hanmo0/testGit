# include <stdio.h>

int add(int a, int b)
{
    int sum;
    sum = a + b;
    return sum;
}

int main()
{
    int a = 1, b;

    printf("input two numbers:\r\n");
    scanf("%d %d", &a, &b);
    printf("sum is %d", add(a, b));
    return 0;
}
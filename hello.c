# include <stdio.h>

int add(int a, int b)
{
    int sum;
    sum = a + b;
    return sum;
}

int main()
{
    int a, b, c;

    printf("input two numbers:\r\n");
    scanf("%d %d", &a, &b);
    c = add(a, b);
    c = add(a, c);
    printf("sum is %d", c);
    return 0;
}
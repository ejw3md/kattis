#include <stdio.h>
#include <stdlib.h>

void print(int *arr, int  n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

}

double area(int *x, int *y, int n)
{
    double a = 0;
    int j = n-1;
    for(int i=0; i<n; i++)
    {
        int before = x[j] + x[i];
        int after = y[j] - y[i];
        a += before*after;
        j=i;
    }
    return a/2.0;

}

double do_it()
{
    int points;
    scanf("%d", &points);
    if( points == 0 )
    {
        return 0;
    }
    int *x = malloc(sizeof(int) * points);
    int *y = malloc(sizeof(int) * points);
    int xtemp, ytemp;
    for(int i=0; i<points; i++)
    {
        scanf("%d %d", &xtemp, &ytemp);
        x[i] = xtemp;
        y[i] = ytemp;
    }
    double a = area(x, y, points);
    free(x);
    free(y);
    return a;

}
int main()
{
    double a = do_it();
    while( a != 0 )
    {
        a < 0 ? printf("CCW  %.1f\n", a*-1): printf("CW  %.1f\n", a);
        a = do_it();
    }

    return 0;
}
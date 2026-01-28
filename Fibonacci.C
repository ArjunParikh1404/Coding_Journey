/*Fibonacci Series */
#include <stdio.h>

int main()
{
    int len, first=0, second=1, sum;
    printf("Enter the length how long do you need series");
    scanf("%d",&len);
    
    if (len == 0)
    {
        printf("Please enter a positive number.\n");
    }

    for (int i=1; i<=len; i++)
    {
        if (i == 1)
        {
            printf("%d ",first);
        }
        else if (i == 2) {
            printf("%d ",second);
        }
        else{
            sum = first + second ;
            printf("%d ",sum);
            
            first = second;
            second = sum;
        }
    }

    return 0;
}

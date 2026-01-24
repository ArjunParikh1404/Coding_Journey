#include <stdio.h>

int main()
{
    int no, b, sum=0;
    printf("Shree Ganeshay Namah: \n");
    
    printf("Give me three digit number for checking is it armstrong or not ?");
    scanf("%d",&no);
    
    b = no;
    
    for (int i=1; i<=3; i++)
    {
        sum = sum + (no%10) * (no%10) * (no%10);
        no = no/10;
    }

    if(sum == b)
    {
        printf("Given number is armstrong");
    }
    else
    {
        printf("Given Number is not armstrong");
    }
    return 0;
}

/* Armstrong Number*/ 

#include <stdio.h>

int main()
{
    int no, b, count=0, sum=0, mul=1;
    
    printf("Enter any number for checking is it armstrong or not ?");
    scanf("%d",&no);
    
    b = no;
    
    while(no != 0)
    {
        count = count + 1;
        no = no/10;
    }
    
    no = b;

    for(int i=1; i <= count; i++)
    {
        for(int j=1; j <= count; j++)
        {
            mul = mul * (no%10);
        }
        
        sum = sum + mul;
        no = no/10;
        mul =1;
    }
    
    if (sum == b)
    {
        printf("Given number is Armstrong");
    }
    else 
    {
        printf("Given number is not Armstrong");
    }

    return 0;
}

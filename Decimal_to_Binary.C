/* Decimal to Binary Conversion */

#include <stdio.h>

int binary(int a){
    
    int digit, temp=0;
    
    while (a != 0)
    {
        digit = a%2;
        temp = temp*10 + digit;
        a = a/2;
    }
    return temp;
}

int main()
{
    int no, digit=0, ans=0, temp;
    
    printf("Enter the number");
    scanf("%d",&no);
    
    temp = binary(no);
    
    while (temp != 0)
    {
        digit = temp%10;
        ans = ans*10 + digit;
        temp = temp/10;
    }
    printf("%d",ans);
    return 0;
}

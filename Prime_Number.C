/*Prime number*/

#include <stdio.h>

int main()
{
    int no, flag = 0;
    printf("Enter the Number");
    scanf("%d",&no);
    
    if(no == 0 || no == 1)
    {
        printf("Given number is neither Prime number nor composite");
    }
    
    else{
        for (int i=2; i*i<=no; i++)
        {
            if (no % i == 0)
            {
                flag = 1;
                break;
            }
        }
        
        if (flag == 1)
        {
            printf("Given number is not a Prime number");
        }
        else 
        {
            printf("Given number is Prime Number");
        }
    }
    return 0;
}

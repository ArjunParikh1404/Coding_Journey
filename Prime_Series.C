/* Series of Prime Numbers*/

#include <stdio.h>

int main()
{
    int Sno, Eno, flag=0;
    
    printf("Enter Starting Point ");
    scanf("%d",&Sno);
    
    printf("Enter Ending Point ");
    scanf("%d",&Eno);
    
    for(int i= Sno; i<= Eno; i++)
    {
        if (i <= 1)
            continue;   

        for (int j=2; j*j <= i; j++)
        {
            if(i % j == 0)
            {
                flag = 1;
                break;
            }
        }
        
        if (flag == 0)
        {
            printf("%d ",i);
        }

        flag = 0;
    }
    
    return 0;
}

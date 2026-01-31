/* Check whether the given number is binary */

#include <stdio.h>
int main()
{
  int no;
  
    printf("Enter the number");
    scanf("%d",&no);
    
    if(no == 0)
    {    
        printf("Number is Binary");
        return 0;    
    }
    
    while(no != 0)
    {
      if(no%10 != 1 && no%10 != 0)
      {
        printf("Number is not Binary");
        return 0;    

      }
      no = no/10;
    }

    printf("Number is Binary");
    return 0;    
}

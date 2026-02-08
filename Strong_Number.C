/* Check if the number is a Strong number 
ex. 145 = 1! + 4! + 5! */

#include <stdio.h>

int factorial(int no)
{
    int fact = 1;
    
    while(no != 0)
    {
        fact = fact * no;
        no--;
    }
    return fact;
}

int main()
{
    int no, checker, reminder, total =0;
    printf("Enter the number: ");
    scanf("%d",&no);
    
    checker = no;
    
    while(no != 0)
    {
        reminder = no % 10;
        reminder = factorial(reminder);
        
        total = total + reminder;
        no = no/10;
    }

    if(checker == total)
        printf("%d is a Strong Number",checker);
        
    else
        printf("%d is not a Strong Number",checker);
        
        
    return 0;
}

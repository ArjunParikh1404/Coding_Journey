#include <stdio.h>

int main()
{
    int no, i=0, number, count=0, n;
    printf("Enter the Number:");
    scanf("%d", &no);
    
    while (i >= 0)
    {
        number = i;
        while (number != 0){
            if(number%10 == 0 || number%10 == 1){
                number = number/10;
                
                if (number == 0)
                    count++;
                    
            }else{
                break;
            }
        }
        
        if(count == no){
            printf("Binary value of %d is %d", no, i);
            break;
        }
        
        i++;
    }
    return 0;
}

/*
Program to generate a progressive string pattern using nested loops

Hello

H
He
Hel
Hell
Hello
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char name[100];
    int count;
    
    printf("Enter the string: ");
    scanf("%99s", name);

    count = strlen(name);
    
    for(int i=1; i<=count; i++)
    {
        for(int j=0; j<i; j++)
        {
            printf("%c",name[j]);
        }
        printf("\n");
    }
    return 0;
}

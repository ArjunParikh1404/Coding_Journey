/* Program to check balanced parentheses in a string (Bracket matcher)*/

#include <stdio.h>

int main()
{
    char str[100];
    int balance = 0;

    printf("Enter the string: ");
    scanf("%99s", str);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '(')
        {
            balance++;
        }
        else if (str[i] == ')')
        {
            balance--;
        }

        if (balance < 0)
        {
            printf("0");
            return 0;
        }
    }

    if (balance == 0)
        printf("1");
    else
        printf("0");

    return 0;
}

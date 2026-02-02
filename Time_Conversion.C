/* Program to convert time from minutes into hours and minutes */

#include <stdio.h>

int main()
{
    int time;
    printf("Enter time in minutes");
    scanf("%d",&time);
    
    printf("%d Hours and %d Minutes", time/60, time%60);
    
    return 0;
}

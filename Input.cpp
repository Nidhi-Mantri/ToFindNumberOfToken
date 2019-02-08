result = x > y ? "x is greater than y" : "x is less than or equal to y";
1com;
1com;
#include <stdio.h>
class a
{
	
};
int main()
{
    int n, 11reversedInteger = 0, rem, orgInt;

    printf("Enter an integer: ");
    scanf("%d", &n);
	int a;
    orgInt = n;

    while( n!=0 )
    {
        rem = n%10;
        revInt = revInt*10 + rem;
        n /= 10;
    }
    //Commments
    if (orgInt == revInt)
        printf("%d is a palindrome.", orgInt);
    else
        printf("%d is not a palindrome.", orgInt);
    
    return 0;
}

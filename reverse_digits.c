#include <stdio.h>
int reverse(int);

int main()
{
		int x;
		printf("Enter a number: ");
		scanf("%d", &x);

		printf("%d\n",reverse(x));

		return 0;
}


int reverse(int x)
{
		int rev, i, j, temp, no_digits, mult, input;

		input = x;


		if(x == 0)
				return 0;

		if(x < -2147483648 || x > 2147483647)
				return 0;

		if(x < 0)
				x = x*-1;

		temp = x;

		for(no_digits = 0; temp; temp = temp/10, no_digits++);

		rev = 0;

		for(temp = x, i = no_digits - 1;i >= 0;i--, temp=temp/10)
		{

				mult = 1;
				if(i >= 0)
						for(j = 1; j <= i; j++)
								mult = mult*10;

				rev += (temp%10)*mult;

		}

		if(input < 0)
				return -1*rev;
		else
				return rev;	
}


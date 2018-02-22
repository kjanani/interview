#include <stdio.h>
#include <stdbool.h>

bool oddEven();

int main()
{
	int x = 10;
	for(int i = 0; i < x; i++)
	{
		printf("%d,%d\n", i,oddEven());
	}
	return 0;
}

bool oddEven()
{
	static bool x = 0;
	
	x = x & 1;
	return x;
}



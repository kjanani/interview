#include <stdio.h>
#define SIZE 1000;

int needle_in_haystack(char *, char *);

int main()
{
	char hay[1000];
	char needle[1000];

	printf("Enter haystack: ");
	scanf("%s",hay);

	printf("Enter needle: ");
	scanf("%s", needle);


	printf("%d\n", needle_in_haystack(hay,needle));

	return 0;	
}

int needle_in_haystack(char *hay, char* needle)
{

	int i, j, length_hay, length_needle, start;

	for(i = 0; hay[i]; i++);
	length_hay = i;

	for(i = 0; needle[i]; i++);
	length_needle = i;

	for(i = 0;hay[i] ;i++)
	{
		start = i;
		for(j = 0; needle[j]; j++,start++)
		{
			if(hay[start] == '\0')
				break;
			if(hay[start] != needle[j])
				break;
		}
		if(j == length_needle)
		{
			return start - length_needle;
		}
	}

	return -1;

}

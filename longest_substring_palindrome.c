#include <stdio.h>
#include <stdlib.h>

char* longestPalindrome(char *);

int main()
{
		char s[1002];
		printf("Enter string: ");
		scanf("%s",s);

		printf("%s",longestPalindrome(s));
		printf("\n");



		return 0;
}



char* longestPalindrome(char* s) 
{
		int length, i, j, mid, start, end, pal_length, max_odd, max_even;
		int PAL_LEN_ODD[1002], PAL_LEN_EVEN[1002];
		char *longest;
	   	longest = malloc(1002*sizeof(char));

		for(i = 0; i < 1002; i++)
		{
			PAL_LEN_ODD[i] = 1;
			PAL_LEN_EVEN[i] = 1;
		}


		for(length = 0; s[length]; length++);

		printf("length = %d\n",length);

		for(i = 1; i < length; i++)
		{
				// for odd
				if(i < length - 1)
				{
					pal_length = 1, mid = i, start = i-1, end = i+1;
					while(start >= 0 && end <= length-1)
					{
						if(s[start] == s[end])
						{
								pal_length += 2;
								start--;
								end++;
						}
						else
								break;
					}

					PAL_LEN_ODD[mid] = pal_length;
				}
				
				// for even
				pal_length = 0; start = (int)(i - 0.5); end = (int)(i+0.5);
				while(start >= 0 && end <= length-1)
				{
						if(s[start] == s[end])
						{
								pal_length += 2;
								start--;
								end++;
						}
						else
								break;
				}

				if(start < 0)
					PAL_LEN_EVEN[0] = pal_length;
				else
					PAL_LEN_EVEN[start+1] = pal_length;
				
		}

		max_odd = -1;
		for(i = 0; i < length; i++)
		{
				if(PAL_LEN_ODD[i] >= max_odd)
				{
						max_odd = PAL_LEN_ODD[i];
						mid = i;
				}
		}
		max_even = -1;
		for(i = 0; i < length; i++)
		{
				if(PAL_LEN_EVEN[i] >= max_even)
				{
					max_even = PAL_LEN_EVEN[i];
					start = i;
				}
		}
		
		if(max_odd >= max_even)
		{
			for(j = 0, i = mid - max_odd/2; i <= mid + max_odd/2; i++, j++)
			{
				longest[j] = s[i];
			}
			longest[j] = '\0';
		}
		else
		{
			for(j = 0, i = start; i < start + max_even; i++, j++)
			{
				longest[j] = s[i];
			}

			longest[j] = '\0';
		}
		return longest;

}

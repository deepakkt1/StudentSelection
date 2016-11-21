void reverse_string(char *str)
{
    /* skip null */
    if (str == 0)
    {
    	return;
    }

    /* skip empty string */
    if (*str == 0)
    {
    	return;
    }

    /* get range */
    char *start = str;
    char *end = start + strlen(str) - 1; /* -1 for \0 */
    char temp;

    /* reverse */
    while (end > start)
    {
    	/* swap */
    	temp = *start;
    	*start = *end;
    	*end = temp;

    	/* move */
    	++start;
    	--end;
    }
}

void revers(char *str)
{
if(str == 0)
 return;
if(*str == 0)
 return;
char *sta = str;
char *end = str;
while(*(++end)){}
--end;
//char *end = sta + strlen(str)-1;
char tmp;
while(sta < end){
tmp = *sta;
*sta = *end;
*end = tmp;

++sta;
--end;

}

}
int main(void)
{
    char s1[] = "Reverse me!";
    char s2[] = "abc";
    char s3[] = "ab";
    char s4[] = "a";
    char s5[] = "";

    revers(0);

    revers(s2);
    revers(s3);
    revers(s4);
    revers(s5);
	revers(s1);

    printf("%s\n", s1);
    printf("%s\n", s2);
    printf("%s\n", s3);
    printf("%s\n", s4);
    printf("%s\n", s5);

    return 0;
}

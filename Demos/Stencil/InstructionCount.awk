#!/bin/awk -f
BEGIN{FS=";"}
{
	if (NF == 8) S[$1]=$7
} # Store insnCount for each filter Name (size)
END{
	for (i in S)
		printf("%4d %s\n", S[i], i);
}

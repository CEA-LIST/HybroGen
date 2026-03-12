#!/usr/bin/awk -f
BEGIN{FS=";"; InsnSum=0; CycleSum = 0}
{if ($7 != "") {
		InsnSum += $7; # Accumulate generated insn count & timing
		CycleSum += $6;
#		print $6/$7 # Print Cycle / insn generated for 1 experiment
	}
}
END{printf("Mean : %d\n", CycleSum/InsnSum);} # Print mean

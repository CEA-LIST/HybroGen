# set debuginfod enabled off
target remote :5555
break main
break convolution
break convolutionH4
break h2_iflush
display/1i $pc

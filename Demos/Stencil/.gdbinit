# set debuginfod enabled off
target remote :5555
break main
break convolution
break convolutionH4
break h2_iflush
comm
x/90i addr
end
display/1i $pc

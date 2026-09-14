target remote :5555
display/i $pc
break main
break h2_iflush
comm
  x/5i addr
end

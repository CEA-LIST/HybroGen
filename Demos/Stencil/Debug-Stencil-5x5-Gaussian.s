x0 = @In	                                        Stencil :              
w1 = line                                           001 004 006 004 001    
w2 = column                                         004 016 024 016 004    
w3 = imgWidth                                       // 006 024 036 024 006 
	                                                // 004 016 024 016 004 
                                                    // 001 004 006 004 001 
(gdb)
0x760:  sub w4,  w2, #0x2     
0x764:  mv  w11, w4                  						w11/njm2 <- column - 2
0x768:  sub w4,  w2, #0x1
0x76c:  mv  w12, w4                  						w12/njm1 <- column - 1
0x770:  add w4,  w2, #0x1
0x774:  mv  w13, w4                  						w13/njp1 <- column + 1
0x778:  add w4,  w2, #0x2
0x77c:  mv  w14, w4                  						w14/njp1 <- column + 2
0x780:  sub w4,  w1, #0x2    
0x784:  mv  w10, w4                  						w10/ni = line - 2
0x788:  mul w4,  w10, w3
0x78c:  mv  w15, w4                  						w15/stride = ni * imgWidth
0x790:  add w4,  w15, w11/lsl x5,  x4, #2/add x4, x0, x5/ldr w5, [x4]          w5 = ld In[stride+njm2]
0x7a0:  mv  w9,  w5                   						w9 = In[strinde+njm2] * 1

0x7a4:  add w4, w15, w12/lsl x5, x4, #2/add x4, x0, x5/ ldr w5, [x4]
0x7b4:  lsl w6, w5, #2
0x7b8:  add w5, w9, w6               						w5 = In[strinde+njm2] * 4
0x7bc:  mv  w9, w5     

0x7c0:  add  w4, w15, w2/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x7d0:  mov  w6, #0x6 
0x7d4:  mul  w7, w5, w6              						w7 = In[strinde+njm2] * 6
0x7d8:  add  w5, w9, w7
0x7dc:  mv   w9, w5
	
0x7e0:  add  w4, w15, w13/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x7f0:  lsl  w6, w5, #2              						w6 = In[strinde+njm2] * 4
0x7f4:  add  w5, w9, w6
0x7f8:  mv   w9, w5
	
0x7fc:  add  w4, w15, w13/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x80c:  add  w6, w9, w5
0x810:  mv   w9, w6
	
0x814:  sub  w4, w1, #0x1/mv w10, w4						w10 /ni = line - 1
0x81c:  mul  w4, w10, w3 /mv w15, w4                        w15 = ni * imgWidth

0x824:  add  w4, w15, w11/lsl  x5, x4, #2/ add  x4, x0, x5 / ldr  w5, [x4]
0x834:  lsl  w6, w5, #2        								* 4
0x838:  add  w5, w9, w6
0x83c:  mv   w9, w5
	
0x840:  add  w4, w15, w12/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x850:  lsl  w6, w5, #4             						* 16
0x854:  add  w5, w9, w6
0x858:  mv   w9, w5
	
0x85c:  add  w4, w15, w2/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x86c:  mov  w6, #0x18        						        * 24
0x870:  mul  w7, w5, w6
0x874:  add  w5, w9, w7
0x878:  mv   w9, w5
	
0x87c:  add  w4, w15, w13/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x88c:  lsl  w6, w5, #4         						     * 16
0x890:  add  w5, w9, w6
0x894:  mv   w9, w5
	
0x898:  add  w4, w15, w14/lsl  x5, x4, #2/add  x4, x0, x5/ldr  w5, [x4]
0x8a8:  lsl  w6, w5, #2        								* 2
0x8ac:  add  w5, w9, w6
0x8b0:  mv   w9, w5
	
0x8b4:  lsr  w4, w9, #8                                     w4/return sum / 256
0x8b8:  mv   w0, w4
0x8bc:  ret


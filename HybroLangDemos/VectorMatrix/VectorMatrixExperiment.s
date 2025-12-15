	.arch armv8-a
	.file	"VectorMatrixExperiment.c"
	.text
	.align	2
	.global	A64_RET__I_64_1
	.type	A64_RET__I_64_1, %function
A64_RET__I_64_1:
.LFB23:
	.cfi_startproc
	adrp	x1, .LANCHOR0
	ldr	x0, [x1, #:lo12:.LANCHOR0]
	add	x2, x0, 4
	str	x2, [x1, #:lo12:.LANCHOR0]
	mov	w1, 960
	movk	w1, 0xd65f, lsl 16
	str	w1, [x0]
	ret
	.cfi_endproc
.LFE23:
	.size	A64_RET__I_64_1, .-A64_RET__I_64_1
	.align	2
	.global	A64_LDRB_RRI_I_8_1
	.type	A64_LDRB_RRI_I_8_1, %function
A64_LDRB_RRI_I_8_1:
.LFB24:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 10, 12
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 960495616
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE24:
	.size	A64_LDRB_RRI_I_8_1, .-A64_LDRB_RRI_I_8_1
	.align	2
	.global	A64_LDRH_RRI_I_16_1
	.type	A64_LDRH_RRI_I_16_1, %function
A64_LDRH_RRI_I_16_1:
.LFB25:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 10, 12
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 2034237440
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE25:
	.size	A64_LDRH_RRI_I_16_1, .-A64_LDRH_RRI_I_16_1
	.align	2
	.global	A64_LDR_RRI_I_32_1
	.type	A64_LDR_RRI_I_32_1, %function
A64_LDR_RRI_I_32_1:
.LFB26:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 10, 12
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, -1186988032
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE26:
	.size	A64_LDR_RRI_I_32_1, .-A64_LDR_RRI_I_32_1
	.align	2
	.global	A64_LDP_RRI_I_32_2
	.type	A64_LDP_RRI_I_32_2, %function
A64_LDP_RRI_I_32_2:
.LFB27:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 15, 7
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 750780416
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE27:
	.size	A64_LDP_RRI_I_32_2, .-A64_LDP_RRI_I_32_2
	.align	2
	.global	A64_LD1_RR_I_32_4
	.type	A64_LD1_RR_I_32_4, %function
A64_LD1_RR_I_32_4:
.LFB28:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 30720
	movk	w0, 0x4c40, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE28:
	.size	A64_LD1_RR_I_32_4, .-A64_LD1_RR_I_32_4
	.align	2
	.global	A64_LDR_RRI_I_64_1
	.type	A64_LDR_RRI_I_64_1, %function
A64_LDR_RRI_I_64_1:
.LFB29:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 10, 12
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, -130023424
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE29:
	.size	A64_LDR_RRI_I_64_1, .-A64_LDR_RRI_I_64_1
	.align	2
	.global	A64_LDR_RRR_I_64_1
	.type	A64_LDR_RRR_I_64_1, %function
A64_LDR_RRR_I_64_1:
.LFB30:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 55296
	movk	w0, 0xfc60, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE30:
	.size	A64_LDR_RRR_I_64_1, .-A64_LDR_RRR_I_64_1
	.align	2
	.global	A64_MUL_RRR_I_8_8
	.type	A64_MUL_RRR_I_8_8, %function
A64_MUL_RRR_I_8_8:
.LFB31:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0xe20, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE31:
	.size	A64_MUL_RRR_I_8_8, .-A64_MUL_RRR_I_8_8
	.align	2
	.global	A64_MUL_RRR_I_8_16
	.type	A64_MUL_RRR_I_8_16, %function
A64_MUL_RRR_I_8_16:
.LFB32:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0x4e20, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE32:
	.size	A64_MUL_RRR_I_8_16, .-A64_MUL_RRR_I_8_16
	.align	2
	.global	A64_MUL_RRR_I_16_4
	.type	A64_MUL_RRR_I_16_4, %function
A64_MUL_RRR_I_16_4:
.LFB33:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0xe60, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE33:
	.size	A64_MUL_RRR_I_16_4, .-A64_MUL_RRR_I_16_4
	.align	2
	.global	A64_MUL_RRR_I_16_8
	.type	A64_MUL_RRR_I_16_8, %function
A64_MUL_RRR_I_16_8:
.LFB34:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0x4e60, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE34:
	.size	A64_MUL_RRR_I_16_8, .-A64_MUL_RRR_I_16_8
	.align	2
	.global	A64_MUL_RRR_I_32_4
	.type	A64_MUL_RRR_I_32_4, %function
A64_MUL_RRR_I_32_4:
.LFB35:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0x4ea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE35:
	.size	A64_MUL_RRR_I_32_4, .-A64_MUL_RRR_I_32_4
	.align	2
	.global	A64_MUL_RRR_I_32_1
	.type	A64_MUL_RRR_I_32_1, %function
A64_MUL_RRR_I_32_1:
.LFB36:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 31744
	movk	w0, 0x1b00, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE36:
	.size	A64_MUL_RRR_I_32_1, .-A64_MUL_RRR_I_32_1
	.align	2
	.global	A64_MUL_RRR_I_32_2
	.type	A64_MUL_RRR_I_32_2, %function
A64_MUL_RRR_I_32_2:
.LFB37:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 39936
	movk	w0, 0xea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE37:
	.size	A64_MUL_RRR_I_32_2, .-A64_MUL_RRR_I_32_2
	.align	2
	.global	A64_MUL_RRR_I_64_1
	.type	A64_MUL_RRR_I_64_1, %function
A64_MUL_RRR_I_64_1:
.LFB38:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 31744
	movk	w0, 0x9b00, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE38:
	.size	A64_MUL_RRR_I_64_1, .-A64_MUL_RRR_I_64_1
	.align	2
	.global	A64_MOV_RRR_I_8_8
	.type	A64_MOV_RRR_I_8_8, %function
A64_MOV_RRR_I_8_8:
.LFB39:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 7168
	movk	w0, 0xea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE39:
	.size	A64_MOV_RRR_I_8_8, .-A64_MOV_RRR_I_8_8
	.align	2
	.global	A64_MOV_RRR_I_16_8
	.type	A64_MOV_RRR_I_16_8, %function
A64_MOV_RRR_I_16_8:
.LFB40:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 7168
	movk	w0, 0x4ea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE40:
	.size	A64_MOV_RRR_I_16_8, .-A64_MOV_RRR_I_16_8
	.align	2
	.global	A64_MOV_RI_I_32_1
	.type	A64_MOV_RI_I_32_1, %function
A64_MOV_RI_I_32_1:
.LFB41:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 16
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 1384120320
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE41:
	.size	A64_MOV_RI_I_32_1, .-A64_MOV_RI_I_32_1
	.align	2
	.global	A64_MOV_RR_I_32_1
	.type	A64_MOV_RR_I_32_1, %function
A64_MOV_RR_I_32_1:
.LFB42:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 285212672
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE42:
	.size	A64_MOV_RR_I_32_1, .-A64_MOV_RR_I_32_1
	.align	2
	.global	A64_MOV_RR_I_32_2
	.type	A64_MOV_RR_I_32_2, %function
A64_MOV_RR_I_32_2:
.LFB43:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 7168
	movk	w0, 0x4e08, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE43:
	.size	A64_MOV_RR_I_32_2, .-A64_MOV_RR_I_32_2
	.align	2
	.global	A64_MOVI_RI_I_32_2
	.type	A64_MOVI_RI_I_32_2, %function
A64_MOVI_RI_I_32_2:
.LFB44:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 2
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 50176
	movk	w0, 0xf00, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE44:
	.size	A64_MOVI_RI_I_32_2, .-A64_MOVI_RI_I_32_2
	.align	2
	.global	A64_DUP_RR_I_32_1
	.type	A64_DUP_RR_I_32_1, %function
A64_DUP_RR_I_32_1:
.LFB45:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 1024
	movk	w0, 0x5e04, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE45:
	.size	A64_DUP_RR_I_32_1, .-A64_DUP_RR_I_32_1
	.align	2
	.global	A64_DUP_RR_I_32_2
	.type	A64_DUP_RR_I_32_2, %function
A64_DUP_RR_I_32_2:
.LFB46:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 1024
	movk	w0, 0xe04, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE46:
	.size	A64_DUP_RR_I_32_2, .-A64_DUP_RR_I_32_2
	.align	2
	.global	A64_MOV_RR_I_64_1
	.type	A64_MOV_RR_I_64_1, %function
A64_MOV_RR_I_64_1:
.LFB47:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, -1862270976
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE47:
	.size	A64_MOV_RR_I_64_1, .-A64_MOV_RR_I_64_1
	.align	2
	.global	A64_MOV_RI_I_64_1
	.type	A64_MOV_RI_I_64_1, %function
A64_MOV_RI_I_64_1:
.LFB48:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 16
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, -763363328
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE48:
	.size	A64_MOV_RI_I_64_1, .-A64_MOV_RI_I_64_1
	.align	2
	.global	A64_DUP_RR_I_64_2
	.type	A64_DUP_RR_I_64_2, %function
A64_DUP_RR_I_64_2:
.LFB49:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 1024
	movk	w0, 0x4e08, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE49:
	.size	A64_DUP_RR_I_64_2, .-A64_DUP_RR_I_64_2
	.align	2
	.global	A64_DUP_RR_I_64_1
	.type	A64_DUP_RR_I_64_1, %function
A64_DUP_RR_I_64_1:
.LFB50:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w1, w1, 5, 5
	and	w0, w0, 31
	orr	w1, w1, w0
	mov	w0, 1024
	movk	w0, 0x5e08, lsl 16
	orr	w1, w1, w0
	str	w1, [x2]
	ret
	.cfi_endproc
.LFE50:
	.size	A64_DUP_RR_I_64_1, .-A64_DUP_RR_I_64_1
	.align	2
	.global	A64_LSL_RRI_I_32_1
	.type	A64_LSL_RRI_I_32_1, %function
A64_LSL_RRI_I_32_1:
.LFB51:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 6
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 1392508928
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE51:
	.size	A64_LSL_RRI_I_32_1, .-A64_LSL_RRI_I_32_1
	.align	2
	.global	A64_LSL_RRR_I_32_1
	.type	A64_LSL_RRR_I_32_1, %function
A64_LSL_RRR_I_32_1:
.LFB52:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 8192
	movk	w0, 0x1ac0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE52:
	.size	A64_LSL_RRR_I_32_1, .-A64_LSL_RRR_I_32_1
	.align	2
	.global	A64_LSL_RRI_I_64_1
	.type	A64_LSL_RRI_I_64_1, %function
A64_LSL_RRI_I_64_1:
.LFB53:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 6
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, -750780416
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE53:
	.size	A64_LSL_RRI_I_64_1, .-A64_LSL_RRI_I_64_1
	.align	2
	.global	A64_LSL_RRR_I_64_1
	.type	A64_LSL_RRR_I_64_1, %function
A64_LSL_RRR_I_64_1:
.LFB54:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 8192
	movk	w0, 0x9ac0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE54:
	.size	A64_LSL_RRR_I_64_1, .-A64_LSL_RRR_I_64_1
	.align	2
	.global	A64_ADD_RRR_I_8_8
	.type	A64_ADD_RRR_I_8_8, %function
A64_ADD_RRR_I_8_8:
.LFB55:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0xe20, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE55:
	.size	A64_ADD_RRR_I_8_8, .-A64_ADD_RRR_I_8_8
	.align	2
	.global	A64_ADD_RRR_I_8_16
	.type	A64_ADD_RRR_I_8_16, %function
A64_ADD_RRR_I_8_16:
.LFB56:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0x4e20, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE56:
	.size	A64_ADD_RRR_I_8_16, .-A64_ADD_RRR_I_8_16
	.align	2
	.global	A64_ADD_RRR_I_16_4
	.type	A64_ADD_RRR_I_16_4, %function
A64_ADD_RRR_I_16_4:
.LFB57:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0xe60, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE57:
	.size	A64_ADD_RRR_I_16_4, .-A64_ADD_RRR_I_16_4
	.align	2
	.global	A64_ADD_RRR_I_16_8
	.type	A64_ADD_RRR_I_16_8, %function
A64_ADD_RRR_I_16_8:
.LFB58:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0x4e60, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE58:
	.size	A64_ADD_RRR_I_16_8, .-A64_ADD_RRR_I_16_8
	.align	2
	.global	A64_ADD_RRR_I_32_2
	.type	A64_ADD_RRR_I_32_2, %function
A64_ADD_RRR_I_32_2:
.LFB59:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0xea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE59:
	.size	A64_ADD_RRR_I_32_2, .-A64_ADD_RRR_I_32_2
	.align	2
	.global	A64_ADD_RRR_I_32_4
	.type	A64_ADD_RRR_I_32_4, %function
A64_ADD_RRR_I_32_4:
.LFB60:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0x4ea0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE60:
	.size	A64_ADD_RRR_I_32_4, .-A64_ADD_RRR_I_32_4
	.align	2
	.global	A64_ADD_RRR_I_64_2
	.type	A64_ADD_RRR_I_64_2, %function
A64_ADD_RRR_I_64_2:
.LFB61:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 33792
	movk	w0, 0x4ee0, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE61:
	.size	A64_ADD_RRR_I_64_2, .-A64_ADD_RRR_I_64_2
	.align	2
	.global	A64_ADD_RRR_I_64_1
	.type	A64_ADD_RRR_I_64_1, %function
A64_ADD_RRR_I_64_1:
.LFB62:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, -1962934272
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE62:
	.size	A64_ADD_RRR_I_64_1, .-A64_ADD_RRR_I_64_1
	.align	2
	.global	A64_ADD_RRI_I_64_1
	.type	A64_ADD_RRI_I_64_1, %function
A64_ADD_RRI_I_64_1:
.LFB63:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 10, 12
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, -1862270976
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE63:
	.size	A64_ADD_RRI_I_64_1, .-A64_ADD_RRI_I_64_1
	.align	2
	.global	A64_STRB_RRI_I_8_1
	.type	A64_STRB_RRI_I_8_1, %function
A64_STRB_RRI_I_8_1:
.LFB64:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 12, 9
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 1024
	movk	w1, 0x3800, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE64:
	.size	A64_STRB_RRI_I_8_1, .-A64_STRB_RRI_I_8_1
	.align	2
	.global	A64_STRH_RRI_I_16_1
	.type	A64_STRH_RRI_I_16_1, %function
A64_STRH_RRI_I_16_1:
.LFB65:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 12, 9
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 1024
	movk	w1, 0x7800, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE65:
	.size	A64_STRH_RRI_I_16_1, .-A64_STRH_RRI_I_16_1
	.align	2
	.global	A64_ST1_RRI_I_32_4
	.type	A64_ST1_RRI_I_32_4, %function
A64_ST1_RRI_I_32_4:
.LFB66:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 6
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 30720
	movk	w1, 0x4c00, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE66:
	.size	A64_ST1_RRI_I_32_4, .-A64_ST1_RRI_I_32_4
	.align	2
	.global	A64_STR_RRI_I_32_1
	.type	A64_STR_RRI_I_32_1, %function
A64_STR_RRI_I_32_1:
.LFB67:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 12, 9
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 1024
	movk	w1, 0xb800, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE67:
	.size	A64_STR_RRI_I_32_1, .-A64_STR_RRI_I_32_1
	.align	2
	.global	A64_ST1_RR_I_32_4
	.type	A64_ST1_RR_I_32_4, %function
A64_ST1_RR_I_32_4:
.LFB68:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x4, x2, 4
	str	x4, [x3, #:lo12:.LANCHOR0]
	ubfiz	w0, w0, 5, 5
	and	w1, w1, 31
	orr	w0, w0, w1
	mov	w1, 30720
	movk	w1, 0x4c00, lsl 16
	orr	w0, w0, w1
	str	w0, [x2]
	ret
	.cfi_endproc
.LFE68:
	.size	A64_ST1_RR_I_32_4, .-A64_ST1_RR_I_32_4
	.align	2
	.global	A64_STR_RRR_I_32_1
	.type	A64_STR_RRR_I_32_1, %function
A64_STR_RRR_I_32_1:
.LFB69:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 55296
	movk	w1, 0xb820, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE69:
	.size	A64_STR_RRR_I_32_1, .-A64_STR_RRR_I_32_1
	.align	2
	.global	A64_STR_RRI_I_32_2
	.type	A64_STR_RRI_I_32_2, %function
A64_STR_RRI_I_32_2:
.LFB70:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 12, 9
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	orr	w0, w0, -67108864
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE70:
	.size	A64_STR_RRI_I_32_2, .-A64_STR_RRI_I_32_2
	.align	2
	.global	A64_STR_RRI_I_64_1
	.type	A64_STR_RRI_I_64_1, %function
A64_STR_RRI_I_64_1:
.LFB71:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 12, 9
	and	w1, w1, 31
	orr	w2, w2, w1
	ubfiz	w0, w0, 5, 5
	mov	w1, 1024
	movk	w1, 0xf800, lsl 16
	orr	w0, w0, w1
	orr	w2, w2, w0
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE71:
	.size	A64_STR_RRI_I_64_1, .-A64_STR_RRI_I_64_1
	.align	2
	.global	A64_STR_RRR_I_64_1
	.type	A64_STR_RRR_I_64_1, %function
A64_STR_RRR_I_64_1:
.LFB72:
	.cfi_startproc
	adrp	x4, .LANCHOR0
	ldr	x3, [x4, #:lo12:.LANCHOR0]
	add	x5, x3, 4
	str	x5, [x4, #:lo12:.LANCHOR0]
	ubfiz	w2, w2, 16, 5
	and	w0, w0, 31
	orr	w2, w2, w0
	ubfiz	w1, w1, 5, 5
	mov	w0, 55296
	movk	w0, 0xf820, lsl 16
	orr	w1, w1, w0
	orr	w2, w2, w1
	str	w2, [x3]
	ret
	.cfi_endproc
.LFE72:
	.size	A64_STR_RRR_I_64_1, .-A64_STR_RRR_I_64_1
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align	3
.LC10:
	.string	"REG"
	.align	3
.LC11:
	.string	"VAL"
	.align	3
.LC12:
	.string	"Warning, W instruction generation failed"
	.align	3
.LC13:
	.string	"ValOrReg / arith / vLen / wLen / regNro / valueImm"
	.align	3
.LC14:
	.string	"P%d: %s/%c/%d/%d/%d\n"
	.text
	.align	2
	.global	aarch64_genW_3
	.type	aarch64_genW_3, %function
aarch64_genW_3:
.LFB73:
	.cfi_startproc
	stp	x29, x30, [sp, -112]!
	.cfi_def_cfa_offset 112
	.cfi_offset 29, -112
	.cfi_offset 30, -104
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	stp	x27, x28, [sp, 80]
	.cfi_offset 19, -96
	.cfi_offset 20, -88
	.cfi_offset 21, -80
	.cfi_offset 22, -72
	.cfi_offset 23, -64
	.cfi_offset 24, -56
	.cfi_offset 25, -48
	.cfi_offset 26, -40
	.cfi_offset 27, -32
	.cfi_offset 28, -24
	mov	x19, x0
	ldr	w6, [x0]
	ldrb	w26, [x0, 4]
	ldr	w27, [x0, 8]
	ldr	w20, [x0, 12]
	ldr	w0, [x0, 16]
	ldr	w3, [x1]
	ldrb	w21, [x1, 4]
	ldr	w24, [x1, 8]
	ldr	w25, [x1, 12]
	ldr	w10, [x1, 16]
	ldr	w22, [x1, 20]
	ldr	w8, [x2]
	ldr	w1, [x2, 16]
	ldr	w11, [x2, 20]
	cmp	w26, 105
	cset	w5, eq
	cmp	w27, 1
	cset	w7, eq
	and	w4, w5, w7
	cmp	w21, 105
	cset	w9, eq
	cmp	w20, 32
	ccmp	w5, 0, 4, le
	cset	w5, ne
	cmp	w7, 0
	ccmp	w9, 0, 4, ne
	cset	w7, ne
	and	w5, w5, w7
	cmp	w22, 0
	ccmp	w3, 1, 0, eq
	cset	w7, eq
	tst	w7, w5
	bne	.L66
	cmp	w6, 0
	cset	w28, eq
	cmp	w3, 0
	cset	w2, eq
	str	w2, [sp, 104]
	orr	w2, w6, w3
	cmp	w2, 0
	ccmp	w24, 1, 0, eq
	cset	w5, eq
	cmp	w25, 32
	ccmp	w9, 0, 4, le
	cset	w2, ne
	cmp	w8, 1
	cset	w7, eq
	ands	w5, w5, w2
	ccmp	w7, 0, 4, ne
	bne	.L67
	orr	w3, w6, w3
	cmp	w3, 0
	cset	w2, eq
	and	w3, w4, w2
	cmp	w8, 0
	cset	w23, eq
	cmp	w5, 0
	ccmp	w23, 0, 4, ne
	bne	.L68
.L56:
	cmp	w20, 64
	cset	w2, le
	and	w3, w3, w2
	cmp	w7, 0
	ccmp	w3, 0, 4, ne
	bne	.L69
	cmp	w3, 0
	ccmp	w23, 0, 4, ne
	bne	.L70
	adrp	x0, .LC12
	add	x0, x0, :lo12:.LC12
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x28, 1
	ldr	w6, [x19, 20]
	mov	w5, w27
	mov	w4, w20
	mov	w3, w26
	csel	x2, x2, x0, eq
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	ldr	x1, [sp, 104]
	tst	x1, 1
	mov	w6, w22
	mov	w5, w24
	mov	w4, w25
	mov	w3, w21
	csel	x2, x2, x0, eq
	mov	w1, 1
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x23, 1
	mov	w6, w22
	mov	w5, w24
	mov	w4, w25
	mov	w3, w21
	csel	x2, x2, x0, eq
	mov	w1, 2
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
.L51:
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x27, x28, [sp, 80]
	ldp	x29, x30, [sp], 112
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 27
	.cfi_restore 28
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L66:
	.cfi_restore_state
	cmp	w8, 1
	cset	w7, eq
	ldrb	w2, [x2, 4]
	cmp	w2, 105
	ccmp	w7, 0, 4, eq
	cset	w4, ne
	cmp	w11, 0
	cset	w2, eq
	and	w3, w4, w2
	tst	w4, w2
	bne	.L71
	cmp	w6, 0
	cset	w28, eq
	cmp	w8, 0
	cset	w23, eq
	str	w3, [sp, 104]
	b	.L56
.L71:
	mov	w2, 0
	mov	w1, 31
	bl	A64_STR_RRI_I_32_1
	b	.L51
.L67:
	mov	w2, w11
	mov	w1, w10
	bl	A64_STR_RRI_I_32_1
	b	.L51
.L68:
	mov	w2, w1
	mov	w1, w10
	bl	A64_STR_RRR_I_32_1
	b	.L51
.L69:
	mov	w2, w11
	mov	w1, w10
	bl	A64_STR_RRI_I_64_1
	b	.L51
.L70:
	mov	w2, w1
	mov	w1, w10
	bl	A64_STR_RRR_I_64_1
	b	.L51
	.cfi_endproc
.LFE73:
	.size	aarch64_genW_3, .-aarch64_genW_3
	.align	2
	.global	aarch64_genRET_0
	.type	aarch64_genRET_0, %function
aarch64_genRET_0:
.LFB74:
	.cfi_startproc
	stp	x29, x30, [sp, -16]!
	.cfi_def_cfa_offset 16
	.cfi_offset 29, -16
	.cfi_offset 30, -8
	mov	x29, sp
	bl	A64_RET__I_64_1
	ldp	x29, x30, [sp], 16
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE74:
	.size	aarch64_genRET_0, .-aarch64_genRET_0
	.section	.rodata.str1.8
	.align	3
.LC15:
	.string	"Optim mv for 0 or 1 (aarch64)"
	.align	3
.LC16:
	.string	"Warning, MV instruction generation failed"
	.text
	.align	2
	.global	aarch64_genMV_3
	.type	aarch64_genMV_3, %function
aarch64_genMV_3:
.LFB75:
	.cfi_startproc
	stp	x29, x30, [sp, -96]!
	.cfi_def_cfa_offset 96
	.cfi_offset 29, -96
	.cfi_offset 30, -88
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	stp	x27, x28, [sp, 80]
	.cfi_offset 19, -80
	.cfi_offset 20, -72
	.cfi_offset 21, -64
	.cfi_offset 22, -56
	.cfi_offset 23, -48
	.cfi_offset 24, -40
	.cfi_offset 25, -32
	.cfi_offset 26, -24
	.cfi_offset 27, -16
	.cfi_offset 28, -8
	mov	x21, x8
	mov	x19, x0
	mov	x20, x1
	ldr	w2, [x0]
	ldrb	w27, [x0, 4]
	ldr	w26, [x0, 8]
	ldr	w23, [x0, 12]
	ldr	w0, [x0, 16]
	ldr	w4, [x1]
	ldrb	w25, [x1, 4]
	ldr	w1, [x1, 16]
	ldr	w28, [x20, 20]
	cmp	w4, 1
	cset	w3, eq
	cmp	w25, 105
	ccmp	w3, 0, 4, eq
	bne	.L90
	cmp	w27, 105
	cset	w6, eq
	cmp	w26, 1
	cset	w5, eq
	cmp	w2, 0
	cset	w22, eq
	cmp	w23, 32
	ccmp	w6, 0, 4, le
	cset	w2, ne
	cmp	w5, 0
	ccmp	w22, 0, 4, ne
	cset	w7, ne
	and	w2, w2, w7
	cmp	w3, 0
	ccmp	w2, 0, 4, ne
	bne	.L84
	cmp	w4, 0
	cset	w24, eq
	cmp	w2, 0
	ccmp	w24, 0, 4, ne
	bne	.L91
	cmp	w23, 64
	ccmp	w22, 0, 4, le
	cset	w2, ne
	cmp	w6, 0
	ccmp	w5, 0, 4, ne
	cset	w4, ne
	and	w2, w2, w4
	cmp	w24, 0
	ccmp	w2, 0, 4, ne
	bne	.L92
.L80:
	cmp	w3, 0
	ccmp	w2, 0, 4, ne
	bne	.L93
	adrp	x0, .LC16
	add	x0, x0, :lo12:.LC16
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x22, 1
	ldr	w6, [x19, 20]
	mov	w5, w26
	mov	w4, w23
	mov	w3, w27
	csel	x2, x2, x0, eq
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x24, 1
	mov	w6, w28
	ldr	w5, [x20, 8]
	ldr	w4, [x20, 12]
	mov	w3, w25
	csel	x2, x2, x0, eq
	mov	w1, 1
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	ldp	x0, x1, [x19]
	stp	x0, x1, [x21]
	ldr	x0, [x19, 16]
	str	x0, [x21, 16]
.L74:
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x27, x28, [sp, 80]
	ldp	x29, x30, [sp], 96
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 27
	.cfi_restore 28
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L90:
	.cfi_restore_state
	cmp	w28, 1
	bls	.L94
	cmp	w27, 105
	cset	w5, eq
	cmp	w26, 1
	cset	w4, eq
	cmp	w2, 0
	cset	w22, eq
	cmp	w5, 0
	ccmp	w4, 0, 4, ne
	mov	w1, 32
	ccmp	w23, w1, 0, ne
	cset	w1, le
	and	w24, w22, w1
	tst	w22, w1
	bne	.L84
	cmp	w23, 64
	ccmp	w22, 0, 4, le
	cset	w2, ne
	cmp	w5, 0
	ccmp	w4, 0, 4, ne
	cset	w1, ne
	and	w2, w2, w1
	b	.L80
.L94:
	adrp	x0, .LC15
	add	x0, x0, :lo12:.LC15
	bl	puts
	ldp	x0, x1, [x20]
	stp	x0, x1, [x21]
	ldr	x0, [x20, 16]
	str	x0, [x21, 16]
	b	.L74
.L84:
	mov	w1, w28
	bl	A64_MOV_RI_I_32_1
	ldp	x0, x1, [x19]
	stp	x0, x1, [x21]
	ldr	x0, [x19, 16]
	str	x0, [x21, 16]
	b	.L74
.L91:
	bl	A64_MOV_RR_I_32_1
	ldp	x0, x1, [x19]
	stp	x0, x1, [x21]
	ldr	x0, [x19, 16]
	str	x0, [x21, 16]
	b	.L74
.L92:
	bl	A64_MOV_RR_I_64_1
	ldp	x0, x1, [x19]
	stp	x0, x1, [x21]
	ldr	x0, [x19, 16]
	str	x0, [x21, 16]
	b	.L74
.L93:
	mov	w1, w28
	bl	A64_MOV_RI_I_64_1
	ldp	x0, x1, [x19]
	stp	x0, x1, [x21]
	ldr	x0, [x19, 16]
	str	x0, [x21, 16]
	b	.L74
	.cfi_endproc
.LFE75:
	.size	aarch64_genMV_3, .-aarch64_genMV_3
	.section	.rodata.str1.8
	.align	3
.LC17:
	.string	"Warning, MUL instruction generation failed"
	.text
	.align	2
	.global	aarch64_genMUL_3
	.type	aarch64_genMUL_3, %function
aarch64_genMUL_3:
.LFB76:
	.cfi_startproc
	stp	x29, x30, [sp, -128]!
	.cfi_def_cfa_offset 128
	.cfi_offset 29, -128
	.cfi_offset 30, -120
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	stp	x27, x28, [sp, 80]
	.cfi_offset 19, -112
	.cfi_offset 20, -104
	.cfi_offset 21, -96
	.cfi_offset 22, -88
	.cfi_offset 23, -80
	.cfi_offset 24, -72
	.cfi_offset 25, -64
	.cfi_offset 26, -56
	.cfi_offset 27, -48
	.cfi_offset 28, -40
	str	x8, [sp, 104]
	mov	x19, x0
	mov	x20, x1
	mov	x21, x2
	ldr	w8, [x0]
	ldrb	w0, [x0, 4]
	str	w0, [sp, 112]
	ldr	w23, [x19, 8]
	ldr	w24, [x19, 12]
	ldr	w0, [x19, 16]
	ldr	w3, [x1]
	ldrb	w7, [x1, 4]
	str	w7, [sp, 116]
	ldr	w1, [x1, 16]
	ldr	w25, [x20, 20]
	ldr	w4, [x2]
	ldrb	w28, [x2, 4]
	ldr	w2, [x2, 16]
	ldr	w22, [x21, 20]
	cmp	w28, 105
	cset	w5, eq
	cmp	w4, 1
	cset	w6, eq
	and	w5, w5, w6
	cmp	w22, 0
	ccmp	w5, 0, 4, eq
	bne	.L96
	cmp	w3, 1
	cset	w6, eq
	cmp	w7, 105
	cset	w7, eq
	and	w6, w6, w7
	cmp	w25, 0
	ccmp	w6, 0, 4, eq
	bne	.L96
	cmp	w5, 0
	ccmp	w22, 1, 0, ne
	beq	.L120
	cmp	w25, 1
	cset	w9, eq
	and	w7, w6, w9
	tst	w6, w9
	bne	.L121
	cmp	w22, 0
	ccmp	w5, 0, 4, ne
	bne	.L122
	ldr	w5, [sp, 112]
	cmp	w5, 105
	cset	w5, eq
	cmp	w24, 8
	cset	w6, le
	cmp	w23, 8
	cset	w9, eq
	cmp	w8, 0
	cset	w27, eq
	cmp	w3, 0
	cset	w7, eq
	str	w7, [sp, 120]
	cmp	w4, 0
	cset	w26, eq
	orr	w7, w8, w3
	orr	w7, w7, w4
	ands	w6, w5, w6
	ccmp	w9, 0, 4, ne
	ccmp	w7, 0, 0, ne
	beq	.L123
	orr	w4, w3, w4
	cmp	w4, 0
	cset	w4, eq
	orr	w3, w8, w3
	cmp	w3, 0
	cset	w8, eq
	cmp	w9, 0
	ccmp	w27, 0, 4, ne
	cset	w7, ne
	and	w7, w4, w7
	cmp	w6, 0
	ccmp	w27, 0, 4, ne
	ccmp	w4, 0, 4, ne
	ccmp	w23, 16, 0, ne
	beq	.L124
.L106:
	cmp	w24, 16
	cset	w3, le
	cmp	w26, 0
	ccmp	w23, 4, 0, ne
	cset	w4, eq
	and	w4, w8, w4
	ands	w3, w5, w3
	ccmp	w4, 0, 4, ne
	bne	.L125
	cmp	w7, 0
	ccmp	w3, 0, 4, ne
	bne	.L126
	cmp	w24, 32
	cset	w3, le
	ands	w3, w5, w3
	ccmp	w4, 0, 4, ne
	bne	.L127
	cmp	w26, 0
	ccmp	w23, 1, 0, ne
	ccmp	w8, 0, 4, eq
	ccmp	w3, 0, 4, ne
	bne	.L128
	adrp	x0, .LC17
	add	x0, x0, :lo12:.LC17
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x27, 1
	ldr	w6, [x19, 20]
	mov	w5, w23
	mov	w4, w24
	ldr	w3, [sp, 112]
	csel	x2, x2, x0, eq
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	ldr	x1, [sp, 120]
	tst	x1, 1
	mov	w6, w25
	ldr	w5, [x20, 8]
	ldr	w4, [x20, 12]
	ldr	w3, [sp, 116]
	csel	x2, x2, x0, eq
	mov	w1, 1
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x26, 1
	mov	w6, w22
	ldr	w5, [x21, 8]
	ldr	w4, [x21, 12]
	mov	w3, w28
	csel	x2, x2, x0, eq
	mov	w1, 2
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
.L95:
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x27, x28, [sp, 80]
	ldp	x29, x30, [sp], 128
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 27
	.cfi_restore 28
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L96:
	.cfi_restore_state
	adrp	x0, .LANCHOR1
	add	x0, x0, :lo12:.LANCHOR1
	ldp	x2, x3, [x0]
	ldr	x1, [sp, 104]
	stp	x2, x3, [x1]
	ldr	x0, [x0, 16]
	str	x0, [x1, 16]
	b	.L95
.L120:
	ldp	x0, x1, [x20]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x20, 16]
	str	x0, [x2, 16]
	b	.L95
.L121:
	ldp	x0, x1, [x21]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x21, 16]
	str	x0, [x2, 16]
	b	.L95
.L122:
	sub	w4, w22, #1
	ands	w4, w4, w22
	beq	.L129
	ldr	w4, [sp, 112]
	cmp	w4, 105
	cset	w5, eq
	cmp	w8, 0
	cset	w27, eq
	cmp	w3, 0
	cset	w4, eq
	str	w4, [sp, 120]
	orr	w8, w8, w3
	cmp	w8, 0
	cset	w8, eq
	mov	w26, w7
	b	.L106
.L129:
	asr	w22, w22, 1
	cbz	w22, .L114
.L104:
	add	w4, w4, 1
	asr	w22, w22, 1
	cbnz	w22, .L104
.L103:
	adrp	x3, .LANCHOR0
	ldr	x2, [x3, #:lo12:.LANCHOR0]
	add	x5, x2, 4
	str	x5, [x3, #:lo12:.LANCHOR0]
	ubfiz	w4, w4, 16, 6
	and	w0, w0, 31
	orr	w4, w4, w0
	ubfiz	w0, w1, 5, 5
	mov	w1, -750780416
	orr	w0, w0, w1
	orr	w4, w4, w0
	str	w4, [x2]
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L114:
	mov	w4, w22
	b	.L103
.L123:
	bl	A64_MUL_RRR_I_8_8
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L124:
	bl	A64_MUL_RRR_I_8_16
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L125:
	bl	A64_MUL_RRR_I_16_4
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L126:
	bl	A64_MUL_RRR_I_16_8
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L127:
	bl	A64_MUL_RRR_I_32_4
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
.L128:
	bl	A64_MUL_RRR_I_32_1
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L95
	.cfi_endproc
.LFE76:
	.size	aarch64_genMUL_3, .-aarch64_genMUL_3
	.section	.rodata.str1.8
	.align	3
.LC18:
	.string	"Optim add for 0  (aarch64)"
	.align	3
.LC19:
	.string	"Warning, ADD instruction generation failed"
	.text
	.align	2
	.global	aarch64_genADD_3
	.type	aarch64_genADD_3, %function
aarch64_genADD_3:
.LFB77:
	.cfi_startproc
	stp	x29, x30, [sp, -128]!
	.cfi_def_cfa_offset 128
	.cfi_offset 29, -128
	.cfi_offset 30, -120
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	stp	x27, x28, [sp, 80]
	.cfi_offset 19, -112
	.cfi_offset 20, -104
	.cfi_offset 21, -96
	.cfi_offset 22, -88
	.cfi_offset 23, -80
	.cfi_offset 24, -72
	.cfi_offset 25, -64
	.cfi_offset 26, -56
	.cfi_offset 27, -48
	.cfi_offset 28, -40
	str	x8, [sp, 104]
	mov	x19, x0
	mov	x20, x1
	mov	x21, x2
	ldr	w3, [x0]
	ldrb	w0, [x0, 4]
	str	w0, [sp, 100]
	ldr	w28, [x19, 8]
	ldr	w27, [x19, 12]
	ldr	w0, [x19, 16]
	ldr	w4, [x1]
	ldrb	w25, [x1, 4]
	ldr	w1, [x1, 16]
	ldr	w26, [x20, 20]
	ldr	w5, [x2]
	ldrb	w23, [x2, 4]
	ldr	w2, [x2, 16]
	ldr	w24, [x21, 20]
	cmp	w5, 1
	cset	w6, eq
	cmp	w23, 105
	ccmp	w6, 0, 4, eq
	ccmp	w24, 0, 0, ne
	beq	.L147
	cmp	w25, 105
	ccmp	w4, 1, 0, eq
	cset	w8, eq
	cmp	w26, 0
	cset	w7, eq
	and	w22, w8, w7
	tst	w8, w7
	bne	.L148
	cmp	w3, 0
	cset	w7, eq
	str	w7, [sp, 120]
	cmp	w4, 0
	cset	w7, eq
	str	w7, [sp, 112]
	orr	w3, w3, w4
	cmp	w3, 0
	ccmp	w28, 1, 0, eq
	cset	w3, eq
	cmp	w27, 64
	mov	w4, 105
	ldr	w7, [sp, 100]
	ccmp	w7, w4, 0, le
	cset	w4, eq
	cmp	w5, 0
	cset	w22, eq
	ands	w3, w3, w4
	ccmp	w22, 0, 4, ne
	bne	.L149
.L138:
	cmp	w6, 0
	ccmp	w3, 0, 4, ne
	bne	.L150
.L139:
	adrp	x0, .LC19
	add	x0, x0, :lo12:.LC19
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	ldr	x1, [sp, 120]
	tst	x1, 1
	ldr	w6, [x19, 20]
	mov	w5, w28
	mov	w4, w27
	ldr	w3, [sp, 100]
	csel	x2, x2, x0, eq
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	ldr	x1, [sp, 112]
	tst	x1, 1
	mov	w6, w26
	ldr	w5, [x20, 8]
	ldr	w4, [x20, 12]
	mov	w3, w25
	csel	x2, x2, x0, eq
	mov	w1, 1
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	tst	x22, 1
	mov	w6, w24
	ldr	w5, [x21, 8]
	ldr	w4, [x21, 12]
	mov	w3, w23
	csel	x2, x2, x0, eq
	mov	w1, 2
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
.L130:
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x27, x28, [sp, 80]
	ldp	x29, x30, [sp], 128
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 27
	.cfi_restore 28
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L147:
	.cfi_restore_state
	cmp	w25, 105
	ccmp	w4, 0, 0, eq
	beq	.L151
.L132:
	adrp	x0, .LC18
	add	x0, x0, :lo12:.LC18
	bl	puts
	ldp	x0, x1, [x20]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x20, 16]
	str	x0, [x2, 16]
	b	.L130
.L151:
	cmp	w1, 1
	bhi	.L132
	cmp	w3, 0
	cset	w2, eq
	str	w2, [sp, 120]
	cmp	w4, 0
	cset	w2, eq
	str	w2, [sp, 112]
	orr	w3, w3, w4
	cmp	w3, 0
	ccmp	w28, 1, 0, eq
	cset	w3, eq
	cmp	w27, 64
	mov	w2, 105
	ldr	w4, [sp, 100]
	ccmp	w4, w2, 0, le
	cset	w2, eq
	and	w3, w3, w2
	cmp	w5, 0
	cset	w22, eq
	b	.L138
.L148:
	cmp	w5, 0
	cset	w0, ne
	cmp	w23, 105
	cset	w1, ne
	orr	w4, w0, w1
	str	w4, [sp, 112]
	cbz	w4, .L152
.L136:
	adrp	x0, .LC18
	add	x0, x0, :lo12:.LC18
	bl	puts
	ldp	x0, x1, [x21]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x21, 16]
	str	x0, [x2, 16]
	b	.L130
.L152:
	cmp	w3, 0
	cset	w0, eq
	str	w0, [sp, 120]
	cmp	w2, 1
	bls	.L139
	b	.L136
.L149:
	bl	A64_ADD_RRR_I_64_1
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L130
.L150:
	mov	w2, w24
	bl	A64_ADD_RRI_I_64_1
	ldp	x0, x1, [x19]
	ldr	x2, [sp, 104]
	stp	x0, x1, [x2]
	ldr	x0, [x19, 16]
	str	x0, [x2, 16]
	b	.L130
	.cfi_endproc
.LFE77:
	.size	aarch64_genADD_3, .-aarch64_genADD_3
	.section	.rodata.str1.8
	.align	3
.LC20:
	.string	"Warning, R instruction generation failed"
	.text
	.align	2
	.global	aarch64_genR_3
	.type	aarch64_genR_3, %function
aarch64_genR_3:
.LFB78:
	.cfi_startproc
	stp	x29, x30, [sp, -80]!
	.cfi_def_cfa_offset 80
	.cfi_offset 29, -80
	.cfi_offset 30, -72
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	.cfi_offset 19, -64
	.cfi_offset 20, -56
	.cfi_offset 21, -48
	.cfi_offset 22, -40
	.cfi_offset 23, -32
	.cfi_offset 24, -24
	.cfi_offset 25, -16
	.cfi_offset 26, -8
	mov	x22, x8
	mov	x19, x0
	mov	x20, x1
	ldr	w26, [x0]
	ldrb	w23, [x0, 4]
	ldr	w25, [x0, 8]
	ldr	w24, [x0, 12]
	ldr	w21, [x1]
	orr	w0, w26, w21
	cmp	w0, 0
	ccmp	w25, 1, 0, eq
	cset	w1, eq
	cmp	w24, 32
	mov	w0, 105
	ccmp	w23, w0, 0, le
	cset	w0, eq
	tst	w1, w0
	bne	.L163
	adrp	x0, .LC20
	add	x0, x0, :lo12:.LC20
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	cmp	w26, 0
	ldr	w6, [x19, 20]
	mov	w5, w25
	mov	w4, w24
	mov	w3, w23
	csel	x2, x2, x0, ne
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	adrp	x0, .LC10
	add	x0, x0, :lo12:.LC10
	adrp	x2, .LC11
	add	x2, x2, :lo12:.LC11
	cmp	w21, 0
	csel	x2, x2, x0, ne
.L158:
	ldr	w6, [x20, 20]
	ldr	w5, [x20, 8]
	ldr	w4, [x20, 12]
	ldrb	w3, [x20, 4]
	mov	w1, 1
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
.L156:
	ldp	x0, x1, [x19]
	stp	x0, x1, [x22]
	ldr	x0, [x19, 16]
	str	x0, [x22, 16]
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x29, x30, [sp], 80
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L163:
	.cfi_restore_state
	ldr	w0, [x2]
	cmp	w0, 1
	beq	.L164
	adrp	x0, .LC20
	add	x0, x0, :lo12:.LC20
	bl	puts
	adrp	x0, .LANCHOR0+8
	strb	wzr, [x0, #:lo12:.LANCHOR0+8]
	adrp	x0, .LC13
	add	x0, x0, :lo12:.LC13
	bl	puts
	adrp	x2, .LC10
	add	x21, x2, :lo12:.LC10
	ldr	w6, [x19, 20]
	mov	w5, w25
	mov	w4, w24
	mov	w3, w23
	mov	x2, x21
	mov	w1, 0
	adrp	x0, .LC14
	add	x0, x0, :lo12:.LC14
	bl	printf
	mov	x2, x21
	b	.L158
.L164:
	ldr	w2, [x2, 20]
	ldr	w1, [x20, 16]
	ldr	w0, [x19, 16]
	bl	A64_LDR_RRI_I_64_1
	b	.L156
	.cfi_endproc
.LFE78:
	.size	aarch64_genR_3, .-aarch64_genR_3
	.section	.rodata.str1.8
	.align	3
.LC21:
	.string	"%s:\n"
	.align	3
.LC22:
	.string	"%04d "
	.text
	.align	2
	.global	printMatrix
	.type	printMatrix, %function
printMatrix:
.LFB79:
	.cfi_startproc
	stp	x29, x30, [sp, -64]!
	.cfi_def_cfa_offset 64
	.cfi_offset 29, -64
	.cfi_offset 30, -56
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	str	x23, [sp, 48]
	.cfi_offset 19, -48
	.cfi_offset 20, -40
	.cfi_offset 21, -32
	.cfi_offset 22, -24
	.cfi_offset 23, -16
	mov	x22, x0
	adrp	x0, .LC21
	add	x0, x0, :lo12:.LC21
	bl	printf
	add	x20, x22, 64
	add	x22, x22, 80
	adrp	x21, .LC22
	add	x21, x21, :lo12:.LC22
	mov	w23, 10
.L166:
	sub	x19, x20, #64
.L167:
	ldr	w1, [x19], 16
	mov	x0, x21
	bl	printf
	cmp	x19, x20
	bne	.L167
	mov	w0, w23
	bl	putchar
	add	x20, x20, 4
	cmp	x20, x22
	bne	.L166
	mov	w0, 10
	bl	putchar
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldr	x23, [sp, 48]
	ldp	x29, x30, [sp], 64
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 23
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE79:
	.size	printMatrix, .-printMatrix
	.section	.rodata.str1.8
	.align	3
.LC23:
	.string	"%s:"
	.text
	.align	2
	.global	printVector
	.type	printVector, %function
printVector:
.LFB80:
	.cfi_startproc
	stp	x29, x30, [sp, -48]!
	.cfi_def_cfa_offset 48
	.cfi_offset 29, -48
	.cfi_offset 30, -40
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	str	x21, [sp, 32]
	.cfi_offset 19, -32
	.cfi_offset 20, -24
	.cfi_offset 21, -16
	mov	x21, x0
	adrp	x0, .LC23
	add	x0, x0, :lo12:.LC23
	bl	printf
	mov	x19, 0
	adrp	x20, .LC22
	add	x20, x20, :lo12:.LC22
.L172:
	ldr	w1, [x21, x19, lsl 2]
	mov	x0, x20
	bl	printf
	add	x19, x19, 1
	cmp	x19, 4
	bne	.L172
	mov	w0, 10
	bl	putchar
	ldp	x19, x20, [sp, 16]
	ldr	x21, [sp, 32]
	ldp	x29, x30, [sp], 48
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 21
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE80:
	.size	printVector, .-printVector
	.section	.rodata.str1.8
	.align	3
.LC24:
	.string	"\t\t\t\t\tValue  arith:%c w: %d v: %d v:%d\n"
	.align	3
.LC25:
	.string	"\t\t\t\t\tReg    arith:%c w: %d v: %d r%%:%d\n"
	.text
	.align	2
	.global	printsValue
	.type	printsValue, %function
printsValue:
.LFB83:
	.cfi_startproc
	stp	x29, x30, [sp, -16]!
	.cfi_def_cfa_offset 16
	.cfi_offset 29, -16
	.cfi_offset 30, -8
	mov	x29, sp
	ldrb	w1, [x0, 4]
	ldr	w3, [x0, 8]
	ldr	w2, [x0, 12]
	ldr	w4, [x0]
	cmp	w4, 1
	beq	.L179
	ldr	w4, [x0, 16]
	adrp	x0, .LC25
	add	x0, x0, :lo12:.LC25
	bl	printf
.L175:
	ldp	x29, x30, [sp], 16
	.cfi_remember_state
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
.L179:
	.cfi_restore_state
	ldr	w4, [x0, 20]
	adrp	x0, .LC24
	add	x0, x0, :lo12:.LC24
	bl	printf
	b	.L175
	.cfi_endproc
.LFE83:
	.size	printsValue, .-printsValue
	.section	.rodata.str1.8
	.align	3
.LC26:
	.string	"iflush: mprotect"
	.align	3
.LC27:
	.string	"(iflush) Failed code generation\n"
	.text
	.align	2
	.global	genVectorMatrixProduct
	.type	genVectorMatrixProduct, %function
genVectorMatrixProduct:
.LFB85:
	.cfi_startproc
	sub	sp, sp, #2800
	.cfi_def_cfa_offset 2800
	stp	x29, x30, [sp]
	.cfi_offset 29, -2800
	.cfi_offset 30, -2792
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	stp	x27, x28, [sp, 80]
	.cfi_offset 19, -2784
	.cfi_offset 20, -2776
	.cfi_offset 21, -2768
	.cfi_offset 22, -2760
	.cfi_offset 23, -2752
	.cfi_offset 24, -2744
	.cfi_offset 25, -2736
	.cfi_offset 26, -2728
	.cfi_offset 27, -2720
	.cfi_offset 28, -2712
	mov	x25, x0
	mov	x19, x1
	adrp	x0, .LANCHOR0
	add	x1, x0, :lo12:.LANCHOR0
	str	x25, [x0, #:lo12:.LANCHOR0]
	mov	w0, 1
	strb	w0, [x1, 8]
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	adrp	x21, .LANCHOR1
	add	x20, x21, :lo12:.LANCHOR1
	ldp	x6, x7, [x20, 24]
	add	x0, sp, 1056
	stp	x6, x7, [x0, 112]
	ldr	x8, [x20, 40]
	str	x8, [sp, 1184]
	ldp	x0, x1, [x20, 48]
	add	x2, sp, 1056
	stp	x0, x1, [x2, 88]
	ldr	x0, [x20, 64]
	str	x0, [sp, 1160]
	ldp	x22, x23, [x20]
	mov	x0, x2
	stp	x22, x23, [x2, 64]
	ldr	x24, [x20, 16]
	str	x24, [sp, 1136]
	ldp	x4, x5, [x20, 72]
	stp	x4, x5, [x2, 40]
	ldr	x1, [x20, 88]
	str	x1, [sp, 1112]
	stp	x4, x5, [x2, 16]
	str	x1, [sp, 1088]
	stp	x4, x5, [x2, -8]
	str	x1, [sp, 1064]
	stp	x4, x5, [x2, -32]
	str	x1, [sp, 1040]
	ldp	x2, x3, [x20, 96]
	stp	x2, x3, [x0, -56]
	ldr	x0, [x20, 112]
	str	x0, [sp, 1016]
	add	x9, sp, 1056
	stp	x2, x3, [x9, -80]
	str	x0, [sp, 992]
	stp	x2, x3, [x9, -104]
	str	x0, [sp, 968]
	stp	x2, x3, [x9, -128]
	str	x0, [sp, 944]
	stp	x2, x3, [x9, -152]
	str	x0, [sp, 920]
	stp	x2, x3, [x9, -176]
	str	x0, [sp, 896]
	stp	x2, x3, [x9, -200]
	str	x0, [sp, 872]
	stp	x2, x3, [x9, -224]
	str	x0, [sp, 848]
	stp	x2, x3, [x9, -248]
	str	x0, [sp, 824]
	add	x9, sp, 544
	stp	x2, x3, [x9, 240]
	str	x0, [sp, 800]
	stp	x2, x3, [x9, 216]
	str	x0, [sp, 776]
	stp	x2, x3, [x9, 192]
	str	x0, [sp, 752]
	stp	x2, x3, [x9, 168]
	str	x0, [sp, 728]
	stp	x2, x3, [x9, 144]
	str	x0, [sp, 704]
	stp	x2, x3, [x9, 120]
	str	x0, [sp, 680]
	stp	x2, x3, [x9, 96]
	str	x0, [sp, 656]
	ldp	x2, x3, [x20, 120]
	stp	x2, x3, [x9, 72]
	ldr	x0, [x20, 136]
	str	x0, [sp, 632]
	stp	x2, x3, [x9, 48]
	str	x0, [sp, 608]
	stp	x2, x3, [x9, 24]
	str	x0, [sp, 584]
	stp	x2, x3, [x9]
	str	x0, [sp, 560]
	stp	x2, x3, [x9, -24]
	str	x0, [sp, 536]
	stp	x2, x3, [sp, 496]
	str	x0, [sp, 512]
	stp	x2, x3, [x9, -72]
	str	x0, [sp, 488]
	stp	x2, x3, [sp, 448]
	str	x0, [sp, 464]
	ldp	x2, x3, [x20, 144]
	stp	x2, x3, [x9, -120]
	ldr	x0, [x20, 160]
	str	x0, [sp, 440]
	stp	x2, x3, [sp, 400]
	str	x0, [sp, 416]
	stp	x2, x3, [x9, -168]
	str	x0, [sp, 392]
	stp	x2, x3, [sp, 352]
	str	x0, [sp, 368]
	stp	x2, x3, [x9, -216]
	str	x0, [sp, 344]
	stp	x2, x3, [sp, 304]
	str	x0, [sp, 320]
	add	x9, sp, 512
	stp	x2, x3, [x9, -232]
	str	x0, [sp, 296]
	stp	x2, x3, [sp, 256]
	str	x0, [sp, 272]
	stp	x4, x5, [sp, 224]
	str	x1, [sp, 240]
	stp	x6, x7, [sp, 192]
	str	x8, [sp, 208]
	stp	x22, x23, [sp, 160]
	str	x24, [sp, 176]
	add	x8, sp, 1096
	add	x2, sp, 160
	add	x1, sp, 192
	add	x0, sp, 224
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -56]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1016]
	str	x0, [sp, 176]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 192]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 208]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 64]
	stp	x0, x1, [sp, 224]
	ldr	x0, [sp, 1136]
	str	x0, [sp, 240]
	add	x8, sp, 1000
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -56]
	stp	x2, x3, [sp, 192]
	ldr	x0, [sp, 1016]
	str	x0, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	stp	x22, x23, [sp, 128]
	str	x24, [sp, 144]
	add	x8, sp, 160
	add	x2, sp, 128
	add	x1, sp, 224
	add	x0, sp, 192
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 160]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -56]
	ldr	x0, [sp, 176]
	str	x0, [sp, 1016]
	mov	w26, 1
	str	w26, [sp, 1216]
	mov	w28, 105
	strb	w28, [sp, 1220]
	str	w26, [sp, 1224]
	mov	w27, 32
	str	w27, [sp, 1228]
	str	wzr, [sp, 1232]
	ldr	w0, [x19]
	str	w0, [sp, 1236]
	add	x0, sp, 544
	ldp	x0, x1, [x0, 72]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 632]
	str	x0, [sp, 144]
	ldp	x0, x1, [x2, 160]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1232]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x24, [sp, 208]
	add	x8, sp, 616
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 72]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 632]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -56]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 1016]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, 72]
	ldr	x0, [sp, 144]
	str	x0, [sp, 632]
	ldp	x2, x3, [x20, 168]
	ldr	x0, [x20, 184]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -80]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 992]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 976
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -80]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 992]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x24, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -80]
	ldr	x0, [sp, 144]
	str	x0, [sp, 992]
	str	w26, [sp, 1312]
	strb	w28, [sp, 1316]
	str	w26, [sp, 1320]
	str	w27, [sp, 1324]
	str	wzr, [sp, 1328]
	ldr	w0, [x19, 16]
	str	w0, [sp, 1332]
	add	x0, sp, 544
	ldp	x0, x1, [x0, -120]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 440]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, -256]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1328]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x24, [sp, 208]
	add	x8, sp, 424
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, -120]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 440]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -80]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 992]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 72]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 632]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, -120]
	ldr	x0, [sp, 144]
	str	x0, [sp, 440]
	ldp	x2, x3, [x20, 192]
	ldr	x0, [x20, 208]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -104]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 968]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 952
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -104]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 968]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x24, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -104]
	ldr	x0, [sp, 144]
	str	x0, [sp, 968]
	str	w26, [sp, 1408]
	strb	w28, [sp, 1412]
	str	w26, [sp, 1416]
	str	w27, [sp, 1420]
	str	wzr, [sp, 1424]
	ldr	w0, [x19, 32]
	str	w0, [sp, 1428]
	add	x0, sp, 544
	ldp	x0, x1, [x0, 48]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 608]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, -160]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1424]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x24, [sp, 208]
	add	x8, sp, 592
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 48]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 608]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -104]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 968]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, -120]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 440]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, 48]
	ldr	x0, [sp, 144]
	str	x0, [sp, 608]
	ldp	x2, x3, [x20, 216]
	ldr	x0, [x20, 232]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -128]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 944]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 928
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -128]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 944]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x24, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -128]
	ldr	x0, [sp, 144]
	str	x0, [sp, 944]
	str	w26, [sp, 1504]
	strb	w28, [sp, 1508]
	str	w26, [sp, 1512]
	str	w27, [sp, 1516]
	str	wzr, [sp, 1520]
	ldr	w0, [x19, 48]
	str	w0, [sp, 1524]
	mov	x21, x20
	ldp	x22, x23, [x20]
	ldr	x20, [x20, 16]
	ldp	x0, x1, [sp, 400]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 416]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, -64]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1520]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 400
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 400]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 416]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -128]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 944]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 48]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 608]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 40]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 1112]
	str	x1, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genW_3
	ldp	x2, x3, [x21, 168]
	ldr	x28, [x21, 184]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 16]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 1088]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 112]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1184]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 1072
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -152]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 920]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 64]
	stp	x0, x1, [sp, 192]
	ldr	x0, [sp, 1136]
	str	x0, [sp, 208]
	add	x8, sp, 904
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -152]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 920]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 1056
	stp	x0, x1, [x3, -152]
	ldr	x0, [sp, 144]
	str	x0, [sp, 920]
	mov	w24, w26
	str	w26, [sp, 1624]
	mov	w27, 105
	strb	w27, [sp, 1628]
	str	w26, [sp, 1632]
	mov	w26, 32
	str	w26, [sp, 1636]
	str	wzr, [sp, 1640]
	ldr	w0, [x19, 4]
	str	w0, [sp, 1644]
	add	x0, sp, 544
	ldp	x0, x1, [x0, 24]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 584]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, 56]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1640]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 568
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 24]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 584]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -152]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 920]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, 24]
	ldr	x0, [sp, 144]
	str	x0, [sp, 584]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -176]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 896]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	ldp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 880
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -176]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 896]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -176]
	ldr	x0, [sp, 144]
	str	x0, [sp, 896]
	str	w24, [sp, 1720]
	strb	w27, [sp, 1724]
	str	w24, [sp, 1728]
	str	w26, [sp, 1732]
	str	wzr, [sp, 1736]
	ldr	w0, [x19, 20]
	str	w0, [sp, 1740]
	add	x0, sp, 544
	ldp	x0, x1, [x0, -168]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 392]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, 152]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1736]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 376
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, -168]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 392]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -176]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 896]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 24]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 584]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, -168]
	ldr	x0, [sp, 144]
	str	x0, [sp, 392]
	ldp	x2, x3, [x21, 192]
	ldr	x28, [x21, 208]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -200]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 872]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 856
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -200]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 872]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 1056
	stp	x0, x1, [x3, -200]
	ldr	x0, [sp, 144]
	str	x0, [sp, 872]
	str	w24, [sp, 1816]
	strb	w27, [sp, 1820]
	str	w24, [sp, 1824]
	str	w26, [sp, 1828]
	str	wzr, [sp, 1832]
	ldr	w0, [x19, 36]
	str	w0, [sp, 1836]
	add	x0, sp, 544
	ldp	x0, x1, [x0]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 560]
	str	x0, [sp, 144]
	add	x0, sp, 1568
	ldp	x0, x1, [x0, 248]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1832]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 544
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 560]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -200]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 872]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, -168]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 392]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3]
	ldr	x0, [sp, 144]
	str	x0, [sp, 560]
	ldp	x2, x3, [x21, 216]
	ldr	x0, [x21, 232]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -224]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 848]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 832
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -224]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 848]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 1056
	stp	x0, x1, [x3, -224]
	ldr	x0, [sp, 144]
	str	x0, [sp, 848]
	str	w24, [sp, 1912]
	strb	w27, [sp, 1916]
	str	w24, [sp, 1920]
	str	w26, [sp, 1924]
	str	wzr, [sp, 1928]
	ldr	w0, [x19, 52]
	str	w0, [sp, 1932]
	ldp	x0, x1, [sp, 352]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 368]
	str	x0, [sp, 144]
	add	x0, sp, 2080
	ldp	x0, x1, [x0, -168]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1928]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 352
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 352]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 368]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -224]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 848]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 560]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 16]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 1088]
	str	x1, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genW_3
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -8]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 1064]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 112]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1184]
	str	x0, [sp, 176]
	ldp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 1048
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -248]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 824]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 64]
	stp	x0, x1, [sp, 192]
	ldr	x0, [sp, 1136]
	str	x0, [sp, 208]
	add	x8, sp, 808
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 1056
	ldp	x2, x3, [x0, -248]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 824]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 1056
	stp	x0, x1, [x2, -248]
	ldr	x0, [sp, 144]
	str	x0, [sp, 824]
	mov	w21, w24
	str	w24, [sp, 2032]
	strb	w27, [sp, 2036]
	str	w24, [sp, 2040]
	str	w26, [sp, 2044]
	str	wzr, [sp, 2048]
	ldr	w0, [x19, 8]
	str	w0, [sp, 2052]
	adrp	x24, .LANCHOR1
	add	x24, x24, :lo12:.LANCHOR1
	ldp	x22, x23, [x24]
	ldr	x20, [x24, 16]
	add	x0, sp, 544
	ldp	x0, x1, [x0, -24]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 536]
	str	x0, [sp, 144]
	add	x0, sp, 2080
	ldp	x0, x1, [x0, -48]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2048]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 520
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, -24]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 536]
	str	x0, [sp, 176]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -248]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 824]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, -24]
	ldr	x0, [sp, 144]
	str	x0, [sp, 536]
	ldp	x2, x3, [x24, 168]
	ldr	x28, [x24, 184]
	add	x0, sp, 544
	ldp	x0, x1, [x0, 240]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 800]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 784
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 240]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 800]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, 240]
	ldr	x0, [sp, 144]
	str	x0, [sp, 800]
	str	w21, [sp, 2128]
	strb	w27, [sp, 2132]
	str	w21, [sp, 2136]
	str	w26, [sp, 2140]
	str	wzr, [sp, 2144]
	ldr	w0, [x19, 24]
	str	w0, [sp, 2148]
	ldp	x0, x1, [x3, -216]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 344]
	str	x0, [sp, 144]
	add	x0, sp, 2080
	ldp	x0, x1, [x0, 48]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2144]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 328
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, -216]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 344]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 240]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 800]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, -24]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 536]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, -216]
	ldr	x0, [sp, 144]
	str	x0, [sp, 344]
	ldp	x2, x3, [x24, 192]
	ldr	x0, [x24, 208]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 216]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 776]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 760
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 216]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 776]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, 216]
	ldr	x0, [sp, 144]
	str	x0, [sp, 776]
	str	w21, [sp, 2224]
	strb	w27, [sp, 2228]
	str	w21, [sp, 2232]
	str	w26, [sp, 2236]
	str	wzr, [sp, 2240]
	ldr	w0, [x19, 40]
	str	w0, [sp, 2244]
	ldp	x0, x1, [sp, 496]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 512]
	str	x0, [sp, 144]
	add	x0, sp, 2080
	ldp	x0, x1, [x0, 144]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2240]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 496
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 496]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 512]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 216]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 776]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, -216]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 344]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	stp	x0, x1, [sp, 496]
	ldr	x0, [sp, 144]
	str	x0, [sp, 512]
	ldp	x4, x5, [x24, 216]
	ldr	x24, [x24, 232]
	add	x0, sp, 544
	ldp	x0, x1, [x0, 192]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 752]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	stp	x4, x5, [sp, 112]
	stp	x4, x5, [sp, 192]
	str	x24, [sp, 208]
	add	x8, sp, 736
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 192]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 752]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, 192]
	ldr	x0, [sp, 144]
	str	x0, [sp, 752]
	str	w21, [sp, 2320]
	strb	w27, [sp, 2324]
	str	w21, [sp, 2328]
	str	w26, [sp, 2332]
	str	wzr, [sp, 2336]
	ldr	w0, [x19, 56]
	str	w0, [sp, 2340]
	ldp	x0, x1, [sp, 304]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 320]
	str	x0, [sp, 144]
	add	x0, sp, 2080
	ldp	x0, x1, [x0, 240]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2336]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 304
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 304]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 320]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 192]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 752]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	ldp	x4, x5, [sp, 496]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 512]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -8]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 1064]
	str	x1, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genW_3
	add	x0, sp, 1056
	ldp	x0, x1, [x0, -32]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 1040]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 112]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1184]
	str	x0, [sp, 176]
	ldp	x4, x5, [sp, 112]
	stp	x4, x5, [sp, 192]
	str	x24, [sp, 208]
	add	x8, sp, 1024
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x0, x1, [x0, 168]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 728]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 64]
	stp	x0, x1, [sp, 192]
	ldr	x0, [sp, 1136]
	str	x0, [sp, 208]
	add	x8, sp, 712
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 168]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 728]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, 168]
	ldr	x0, [sp, 144]
	str	x0, [sp, 728]
	str	w21, [sp, 2440]
	strb	w27, [sp, 2444]
	str	w21, [sp, 2448]
	str	w26, [sp, 2452]
	str	wzr, [sp, 2456]
	ldr	w0, [x19, 12]
	str	w0, [sp, 2460]
	ldp	x0, x1, [x3, -72]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 488]
	str	x0, [sp, 144]
	add	x0, sp, 2592
	ldp	x0, x1, [x0, -152]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2456]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 472
	add	x0, sp, 192
	mov	x2, x0
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, -72]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 488]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 168]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 728]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x0, sp, 224
	mov	x2, x0
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x0, x1, [sp, 128]
	add	x3, sp, 544
	stp	x0, x1, [x3, -72]
	ldr	x0, [sp, 144]
	str	x0, [sp, 488]
	ldp	x0, x1, [x3, 144]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 704]
	str	x0, [sp, 144]
	add	x0, sp, 1056
	ldp	x0, x1, [x0, 88]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 1160]
	str	x0, [sp, 176]
	ldp	x2, x3, [sp, 96]
	stp	x2, x3, [sp, 192]
	str	x28, [sp, 208]
	add	x8, sp, 688
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 144]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 704]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x20, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, 144]
	ldr	x0, [sp, 144]
	str	x0, [sp, 704]
	str	w21, [sp, 2536]
	strb	w27, [sp, 2540]
	str	w21, [sp, 2544]
	str	w26, [sp, 2548]
	str	wzr, [sp, 2552]
	ldr	w0, [x19, 28]
	str	w0, [sp, 2556]
	add	x0, sp, 512
	ldp	x0, x1, [x0, -232]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 296]
	str	x0, [sp, 144]
	add	x0, sp, 2592
	ldp	x0, x1, [x0, -56]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2552]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x20, [sp, 208]
	add	x8, sp, 280
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	add	x0, sp, 512
	ldp	x2, x3, [x0, -232]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 296]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 144]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 704]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, -72]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 488]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 512
	stp	x0, x1, [x2, -232]
	ldr	x0, [sp, 144]
	str	x0, [sp, 296]
	adrp	x20, .LANCHOR1
	add	x20, x20, :lo12:.LANCHOR1
	ldp	x2, x3, [x20, 192]
	ldr	x0, [x20, 208]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 120]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 680]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 664
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	ldp	x22, x23, [x20]
	ldr	x21, [x20, 16]
	add	x0, sp, 544
	ldp	x2, x3, [x0, 120]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 680]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x21, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, 120]
	ldr	x0, [sp, 144]
	str	x0, [sp, 680]
	mov	w24, 1
	str	w24, [sp, 2632]
	strb	w27, [sp, 2636]
	str	w24, [sp, 2640]
	str	w26, [sp, 2644]
	str	wzr, [sp, 2648]
	ldr	w0, [x19, 44]
	str	w0, [sp, 2652]
	ldp	x0, x1, [sp, 448]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 464]
	str	x0, [sp, 144]
	add	x0, sp, 2592
	ldp	x0, x1, [x0, 40]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2648]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x21, [sp, 208]
	add	x8, sp, 448
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 448]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 464]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 120]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 680]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	add	x1, sp, 512
	ldp	x4, x5, [x1, -232]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 296]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x0, x1, [sp, 128]
	stp	x0, x1, [sp, 448]
	ldr	x0, [sp, 144]
	str	x0, [sp, 464]
	ldp	x2, x3, [x20, 216]
	ldr	x0, [x20, 232]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 96]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 656]
	str	x1, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, 88]
	stp	x4, x5, [sp, 160]
	ldr	x1, [sp, 1160]
	str	x1, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	add	x8, sp, 640
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genADD_3
	add	x0, sp, 544
	ldp	x2, x3, [x0, 96]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 656]
	str	x0, [sp, 176]
	stp	x2, x3, [sp, 192]
	str	x0, [sp, 208]
	stp	x22, x23, [sp, 224]
	str	x21, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genR_3
	ldp	x0, x1, [sp, 128]
	add	x2, sp, 544
	stp	x0, x1, [x2, 96]
	ldr	x0, [sp, 144]
	str	x0, [sp, 656]
	str	w24, [sp, 2728]
	strb	w27, [sp, 2732]
	str	w24, [sp, 2736]
	str	w26, [sp, 2740]
	str	wzr, [sp, 2744]
	ldr	w0, [x19, 60]
	str	w0, [sp, 2748]
	ldp	x0, x1, [sp, 256]
	stp	x0, x1, [sp, 128]
	ldr	x0, [sp, 272]
	str	x0, [sp, 144]
	add	x0, sp, 2592
	ldp	x0, x1, [x0, 136]
	stp	x0, x1, [sp, 160]
	ldr	x0, [sp, 2744]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x21, [sp, 208]
	add	x8, sp, 256
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genMV_3
	ldp	x2, x3, [sp, 256]
	stp	x2, x3, [sp, 160]
	ldr	x0, [sp, 272]
	str	x0, [sp, 176]
	add	x1, sp, 544
	ldp	x4, x5, [x1, 96]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 656]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genMUL_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	ldp	x4, x5, [sp, 448]
	stp	x4, x5, [sp, 192]
	ldr	x1, [sp, 464]
	str	x1, [sp, 208]
	stp	x2, x3, [sp, 224]
	str	x0, [sp, 240]
	add	x8, sp, 128
	add	x2, sp, 224
	add	x1, sp, 192
	add	x0, sp, 160
	bl	aarch64_genADD_3
	ldp	x2, x3, [sp, 128]
	ldr	x0, [sp, 144]
	add	x1, sp, 1056
	ldp	x4, x5, [x1, -32]
	stp	x4, x5, [sp, 128]
	ldr	x1, [sp, 1040]
	str	x1, [sp, 144]
	stp	x2, x3, [sp, 160]
	str	x0, [sp, 176]
	stp	x22, x23, [sp, 192]
	str	x21, [sp, 208]
	add	x2, sp, 192
	add	x1, sp, 160
	add	x0, sp, 128
	bl	aarch64_genW_3
	bl	A64_RET__I_64_1
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	adrp	x0, .LANCHOR0
	ldr	x19, [x0, #:lo12:.LANCHOR0]
	bl	getpagesize
	sxtw	x0, w0
	neg	x0, x0
	mov	w2, 7
	sub	x1, x19, x25
	and	x0, x25, x0
	bl	mprotect
	cbnz	w0, .L184
	adrp	x0, .LANCHOR0+8
	ldrb	w0, [x0, #:lo12:.LANCHOR0+8]
	tbz	x0, 0, .L185
	mov	x0, x25
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x27, x28, [sp, 80]
	ldp	x29, x30, [sp]
	add	sp, sp, 2800
	.cfi_remember_state
	.cfi_restore 29
	.cfi_restore 30
	.cfi_restore 27
	.cfi_restore 28
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L184:
	.cfi_restore_state
	adrp	x0, .LC26
	add	x0, x0, :lo12:.LC26
	bl	perror
	mov	w0, -1
	bl	exit
.L185:
	adrp	x0, stderr
	ldr	x3, [x0, #:lo12:stderr]
	mov	x2, 32
	mov	x1, 1
	adrp	x0, .LC27
	add	x0, x0, :lo12:.LC27
	bl	fwrite
	mov	w0, -5
	bl	exit
	.cfi_endproc
.LFE85:
	.size	genVectorMatrixProduct, .-genVectorMatrixProduct
	.align	2
	.global	VectorMatrixProduct
	.type	VectorMatrixProduct, %function
VectorMatrixProduct:
.LFB86:
	.cfi_startproc
	mov	x8, x0
	mov	x7, x2
	add	x9, x2, 16
.L188:
	mov	x4, x8
	str	wzr, [x8]
	mov	x2, 0
.L187:
	lsl	x3, x2, 4
	ldr	w3, [x7, x3]
	ldr	w6, [x1, x2, lsl 2]
	ldr	w5, [x4]
	madd	w3, w3, w6, w5
	str	w3, [x4]
	add	x2, x2, 1
	cmp	x2, 4
	bne	.L187
	add	x8, x8, 4
	add	x7, x7, 4
	cmp	x7, x9
	bne	.L188
	ldr	w0, [x0, 12]
	ret
	.cfi_endproc
.LFE86:
	.size	VectorMatrixProduct, .-VectorMatrixProduct
	.section	.rodata.str1.8
	.align	3
.LC28:
	.string	"NOT OK"
	.align	3
.LC29:
	.string	"OK"
	.align	3
.LC30:
	.string	"%4d "
	.align	3
.LC31:
	.string	"%s : "
	.align	3
.LC32:
	.string	" %s\n"
	.text
	.align	2
	.global	vectorCompare
	.type	vectorCompare, %function
vectorCompare:
.LFB87:
	.cfi_startproc
	stp	x29, x30, [sp, -80]!
	.cfi_def_cfa_offset 80
	.cfi_offset 29, -80
	.cfi_offset 30, -72
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	stp	x25, x26, [sp, 64]
	.cfi_offset 19, -64
	.cfi_offset 20, -56
	.cfi_offset 21, -48
	.cfi_offset 22, -40
	.cfi_offset 23, -32
	.cfi_offset 24, -24
	.cfi_offset 25, -16
	.cfi_offset 26, -8
	mov	x23, x0
	mov	x22, x1
	mov	x26, x2
	mov	w21, w3
	mov	x19, 0
	mov	w20, 0
	mov	w24, 1
	adrp	x25, .LC30
	add	x25, x25, :lo12:.LC30
	b	.L194
.L193:
	add	x19, x19, 4
	cmp	x19, 16
	beq	.L200
.L194:
	ldr	w1, [x22, x19]
	ldr	w4, [x23, x19]
	cmp	w4, w1
	csel	w20, w20, w24, eq
	cbz	w21, .L193
	mov	x0, x25
	bl	printf
	b	.L193
.L200:
	mov	x1, x26
	adrp	x0, .LC31
	add	x0, x0, :lo12:.LC31
	bl	printf
	adrp	x0, .LC28
	add	x0, x0, :lo12:.LC28
	adrp	x1, .LC29
	add	x1, x1, :lo12:.LC29
	cmp	w20, 0
	csel	x1, x1, x0, eq
	adrp	x0, .LC32
	add	x0, x0, :lo12:.LC32
	bl	printf
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x25, x26, [sp, 64]
	ldp	x29, x30, [sp], 80
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 25
	.cfi_restore 26
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE87:
	.size	vectorCompare, .-vectorCompare
	.section	.rodata.str1.8
	.align	3
.LC33:
	.string	"Compilette"
	.align	3
.LC34:
	.string	"General    ticks %lu\n"
	.align	3
.LC35:
	.string	"Compilette ticks %lu\n"
	.align	3
.LC36:
	.string	"Accumulator %lu\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB88:
	.cfi_startproc
	stp	x29, x30, [sp, -208]!
	.cfi_def_cfa_offset 208
	.cfi_offset 29, -208
	.cfi_offset 30, -200
	mov	x29, sp
	stp	x19, x20, [sp, 16]
	stp	x21, x22, [sp, 32]
	stp	x23, x24, [sp, 48]
	.cfi_offset 19, -192
	.cfi_offset 20, -184
	.cfi_offset 21, -176
	.cfi_offset 22, -168
	.cfi_offset 23, -160
	.cfi_offset 24, -152
	mov	w0, 5
	str	w0, [sp, 128]
	mov	w0, 6
	str	w0, [sp, 132]
	mov	w0, 7
	str	w0, [sp, 136]
	mov	w0, 8
	str	w0, [sp, 140]
	mov	w0, 9
	str	w0, [sp, 112]
	mov	w0, 10
	str	w0, [sp, 116]
	mov	w0, 11
	str	w0, [sp, 120]
	mov	w0, 12
	str	w0, [sp, 124]
	mov	w0, 13
	str	w0, [sp, 96]
	mov	w0, 14
	str	w0, [sp, 100]
	mov	w0, 15
	str	w0, [sp, 104]
	mov	w0, 16
	str	w0, [sp, 108]
	ldr	x22, [x1, 8]
	add	x20, x1, 16
	add	x21, sp, 144
	mov	w24, 2
	mov	w23, 10
.L202:
	mov	x19, 0
.L203:
	mov	w2, w23
	mov	x1, 0
	ldr	x0, [x20, x19, lsl 3]
	bl	strtol
	str	w0, [x21, x19, lsl 2]
	add	x19, x19, 1
	cmp	x19, 4
	bne	.L203
	add	w24, w24, 4
	add	x20, x20, 32
	add	x21, x21, 16
	cmp	w24, 18
	bne	.L202
	mov	x1, x22
	add	x0, sp, 144
	bl	printMatrix
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w20, 1000
	mov	x19, 0
.L205:
	add	x2, sp, 144
	add	x1, sp, 128
	add	x0, sp, 80
	bl	VectorMatrixProduct
	add	x19, x19, w0, sxtw
	subs	w20, w20, #1
	bne	.L205
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	x1, x22
	add	x0, sp, 80
	bl	printVector
	mov	x0, 1024
	bl	malloc
	add	x1, sp, 144
	bl	genVectorMatrixProduct
	mov	x20, x0
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L206:
	add	x1, sp, 128
	add	x0, sp, 64
	blr	x20
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L206
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	adrp	x1, .LC33
	add	x1, x1, :lo12:.LC33
	add	x0, sp, 64
	bl	printVector
	mov	w3, 1
	mov	x2, x22
	add	x1, sp, 64
	add	x0, sp, 80
	bl	vectorCompare
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L207:
	add	x2, sp, 144
	add	x1, sp, 112
	add	x0, sp, 80
	bl	VectorMatrixProduct
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L207
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	x1, x22
	add	x0, sp, 80
	bl	printVector
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L208:
	add	x1, sp, 112
	add	x0, sp, 64
	blr	x20
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L208
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	adrp	x1, .LC33
	add	x1, x1, :lo12:.LC33
	add	x0, sp, 64
	bl	printVector
	mov	w3, 1
	mov	x2, x22
	add	x1, sp, 64
	add	x0, sp, 80
	bl	vectorCompare
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L209:
	add	x2, sp, 144
	add	x1, sp, 96
	add	x0, sp, 80
	bl	VectorMatrixProduct
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L209
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	x1, x22
	add	x0, sp, 80
	bl	printVector
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L210:
	add	x1, sp, 96
	add	x0, sp, 64
	blr	x20
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L210
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x0,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	adrp	x1, .LC33
	add	x1, x1, :lo12:.LC33
	add	x0, sp, 64
	bl	printVector
	mov	w3, 1
	mov	x2, x22
	add	x1, sp, 64
	add	x0, sp, 80
	bl	vectorCompare
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x24,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L211:
	add	x2, sp, 144
	add	x1, sp, 112
	add	x0, sp, 80
	bl	VectorMatrixProduct
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L211
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x23,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	sub	x23, x23, x24
	mov	x1, x22
	add	x0, sp, 80
	bl	printVector
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x24,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	mov	w21, 1000
.L212:
	add	x1, sp, 112
	add	x0, sp, 64
	blr	x20
	add	x19, x19, w0, sxtw
	subs	w21, w21, #1
	bne	.L212
#APP
// 614 "VectorMatrixExperiment.c" 1
	mrs x20,  CNTVCT_EL0
// 0 "" 2
#NO_APP
	sub	x20, x20, x24
	adrp	x1, .LC33
	add	x1, x1, :lo12:.LC33
	add	x0, sp, 64
	bl	printVector
	mov	w3, 1
	mov	x2, x22
	add	x1, sp, 64
	add	x0, sp, 80
	bl	vectorCompare
	mov	x1, x23
	adrp	x0, .LC34
	add	x0, x0, :lo12:.LC34
	bl	printf
	mov	x1, x20
	adrp	x0, .LC35
	add	x0, x0, :lo12:.LC35
	bl	printf
	mov	x1, x19
	adrp	x0, .LC36
	add	x0, x0, :lo12:.LC36
	bl	printf
	mov	w0, 0
	ldp	x19, x20, [sp, 16]
	ldp	x21, x22, [sp, 32]
	ldp	x23, x24, [sp, 48]
	ldp	x29, x30, [sp], 208
	.cfi_restore 30
	.cfi_restore 29
	.cfi_restore 23
	.cfi_restore 24
	.cfi_restore 21
	.cfi_restore 22
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE88:
	.size	main, .-main
	.global	h2_codeGenerationOK
	.section	.rodata
	.align	3
	.set	.LANCHOR1,. + 0
.LC0:
	.word	1
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	0
	.word	0
.LC1:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	0
	.word	0
.LC2:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	1
	.word	0
.LC3:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	9
	.word	0
.LC4:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	10
	.word	0
.LC5:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	11
	.word	0
.LC6:
	.word	0
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	12
	.word	0
.LC7:
	.word	1
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	0
	.word	4
.LC8:
	.word	1
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	0
	.word	8
.LC9:
	.word	1
	.byte	105
	.zero	3
	.word	1
	.word	32
	.word	0
	.word	12
	.bss
	.align	3
	.set	.LANCHOR0,. + 0
	.type	h2_asm_pc, %object
	.size	h2_asm_pc, 8
h2_asm_pc:
	.zero	8
	.type	h2_codeGenerationOK, %object
	.size	h2_codeGenerationOK, 1
h2_codeGenerationOK:
	.zero	1
	.ident	"GCC: (GNU) 13.2.0"
	.section	.note.GNU-stack,"",@progbits

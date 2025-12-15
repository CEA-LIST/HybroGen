	.arch armv8-a
	.file	"TestStCst.c"
	.text
	.align	2
	.global	StoreNull
	.type	StoreNull, %function
StoreNull:
.LFB0:
	.cfi_startproc
	sub	sp, sp, #64
	.cfi_def_cfa_offset 64
	str	x0, [sp, 8]
	str	wzr, [sp, 60]
	ldr	w0, [sp, 60]
	str	w0, [sp, 56]
	ldr	w0, [sp, 56]
	str	w0, [sp, 52]
	ldr	w0, [sp, 52]
	str	w0, [sp, 48]
	ldr	w0, [sp, 48]
	str	w0, [sp, 44]
	ldr	w0, [sp, 44]
	str	w0, [sp, 40]
	ldr	w0, [sp, 40]
	str	w0, [sp, 36]
	ldr	w0, [sp, 36]
	str	w0, [sp, 32]
	ldr	w0, [sp, 32]
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	str	w0, [sp, 24]
	ldr	w0, [sp, 24]
	str	w0, [sp, 20]
	ldr	w0, [sp, 20]
	str	w0, [sp, 16]
	ldr	x0, [sp, 8]
	ldr	w1, [sp, 16]
	str	w1, [x0]
	nop
	add	sp, sp, 64
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE0:
	.size	StoreNull, .-StoreNull
	.align	2
	.global	StoreOne
	.type	StoreOne, %function
StoreOne:
.LFB1:
	.cfi_startproc
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, 8]
	ldr	x0, [sp, 8]
	mov	w1, 1
	str	w1, [x0]
	nop
	add	sp, sp, 16
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE1:
	.size	StoreOne, .-StoreOne
	.ident	"GCC: (GNU) 13.2.0"
	.section	.note.GNU-stack,"",@progbits

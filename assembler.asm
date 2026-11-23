; Info---
bits 64
default rel ; allows for adresses to be moved 

section .bss; this will hold varibles

section .data ; this will hold constants --> only moved not changed

section .text ; hold the main function --> assembly logic
global main ; int main in C
extern ExitProcess ; terminal can end Assembly program


extern printf
extern scanf
;pulls these functions from C 
;can read user input
;GCC as linker

main: ; entry port

;creating shadow space --> 32 bytes

	 PUSH rbp ; push the base pointer to the top of the stack
	 MOV rbp, rsp ; move the the stack pointer into the base pointer
	 SUB rsp, 32 ; subtract 32 from the bottom of the stack


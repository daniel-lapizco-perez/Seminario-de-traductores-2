.386
.model flat, stdcall
option casemap:none

include c:\masm32\include\masm32rt.inc

.code

suma proc a:DWORD,b:DWORD
mov eax, a
add eax, b
ret
suma endp

main proc
local resultado:DWORD
mov eax, 24
push eax
mov eax, 6
push eax
call suma
mov resultado, eax
mov eax, resultado
print str$(eax)
invoke ExitProcess, 0

main endp
end main
#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

def CplusplusFile( shellcode, win=False):
	import time
	if win == True:
		db = """//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//{0} - {1}
//Compile : gcc shell.c -o shell.exe


#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>
		 
		 
int main(void)
{
	char *shellcode = "{2}";
	DWORD why_must_this_variable;
	BOOL ret = VirtualProtect (shellcode, strlen(shellcode),
	PAGE_EXECUTE_READWRITE, &why_must_this_variable);
		 
	if (!ret) {
		printf ("VirtualProtect");
		return EXIT_FAILURE;
	}
			 
	
	((void (*)(void))shellcode)();
	return EXIT_SUCCESS;
}	



		""".format(time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"), shellcode)

	else:
		db = """//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//{0} - {1}
//Compile : g++ -fno-stack-protector -z execstack shell.cpp -o shell

unsigned char shellcode[] = "{2}";

int main(){
	int (*func)() = (int(*)())shellcode;   
	func();
}
		  
		""".format(time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"), shellcode)


	from .logger import logs
	logs( db, "cpp")



#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - infinty loop
 * Return: 0
 * Ashraf Atef
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - craete a zombies process
 * Return: 0
 * Ashraf Atef
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		int pid = fork();

		if (pid)
			printf("Zombie process created, PID: %d\n", pid);
		else
			infinite_while();
	}
	return (0);
}

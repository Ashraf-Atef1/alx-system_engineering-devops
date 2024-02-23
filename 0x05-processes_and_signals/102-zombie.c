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
	int pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid), sleep(1);
		else
			return (0);
	}
	infinite_while();
	return (0);
}

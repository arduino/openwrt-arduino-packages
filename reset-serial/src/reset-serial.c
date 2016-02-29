#include <asm/termios.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

#define DESIRED_BAUD	250000


int main(int argc, char **argv)
{
	int fd;
	char *device;

	if (argc < 2)
	{
		fprintf(stderr, "usage: %s device\n", argv[0]);
		exit(2);
	}
	device = argv[1];

	/* Open device */
	if ((fd = open(device, O_RDWR|O_NONBLOCK)) < 0)
	{
		perror(device);
		exit(1);
	}

	struct termios2 tio;
	ioctl(fd, TCGETS2, &tio);
	tio.c_cflag &= ~CBAUD;
	tio.c_cflag |= BOTHER;
	tio.c_ispeed = DESIRED_BAUD;
	tio.c_ospeed = DESIRED_BAUD;
	/* do other miscellaneous setup options with the flags here */
	ioctl(fd, TCSETS2, &tio);

	perror("done");
	exit(0);
}


# build helloworld executable when user executes "make"
reset-serial: reset-serial.o
	$(CC) $(LDFLAGS) reset-serial.o -o reset-serial
reset-serial.o: reset-serial.c
	$(CC) $(CFLAGS) -c reset-serial.c

# remove object files and executable when user executes "make clean"
clean:
	rm *.o reset-serial


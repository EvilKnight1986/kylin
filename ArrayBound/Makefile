build ?= arraybound

CC		= gcc
CPP		= g++

CFLAGS	= -g
LDFLAGS = 

#ifeq "$(build)" "stackoverflow"
#	CFLAGS += -g
#else ifeq "$(build)" "stackoverflownx"
#	CFLAGS += -g
#endif

LIBS		= -lpthread

all: ArrayBound ArrayBoundNX ArrayBoundSP

ArrayBound: ArrayBound.c
	$(CC) -o $@  $(CFLAGS) -fno-stack-protector -z execstack -D_FORTIFY_SOURCE=0 $<

ArrayBoundNX: ArrayBound.c
	$(CC) -o $@  $(CFLAGS) -fno-stack-protector -D_FORTIFY_SOURCE=0 $<

ArrayBoundSP: ArrayBound.c
	$(CC) -o $@  $(CFLAGS) $<

clean:
	rm -rf ./*.o

cleanall:
	rm -rf ./*.o ./ArrayBound ./ArrayBoundNX ./ArrayBoundSP


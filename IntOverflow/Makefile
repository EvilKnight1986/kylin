build ?= intoverflow

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

all: IntOverflow IntOverflowNX IntOverflowSP

IntOverflow: IntOverflow.c
	$(CC) -o $@  $(CFLAGS) -fno-stack-protector -z execstack -D_FORTIFY_SOURCE=0 $<

IntOverflowNX: IntOverflow.c
	$(CC) -o $@  $(CFLAGS) -fno-stack-protector -D_FORTIFY_SOURCE=0 $<

IntOverflowSP: IntOverflow.c
	$(CC) -o $@  $(CFLAGS) $<

clean:
	rm -rf ./*.o

cleanall:
	rm -rf ./*.o ./IntOverflow ./IntOverflowNX ./IntOverflowSP


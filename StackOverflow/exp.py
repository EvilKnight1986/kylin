#! /bin/python

from pwn import *
context(arch = 'aarch64', os = 'linux')
r = remote('172.31.21.202', 1234)
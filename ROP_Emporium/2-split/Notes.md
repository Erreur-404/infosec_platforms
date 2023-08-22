I first fetched the necessary addresses to perform the exploit. Since the program uses read, we can use a buffer overflow to overwrite the stack's return address and redirect the execution to an arbitrary address. There is a `system` call in the usefulFunction method, but it is preceded by `/bin/ls`. We can modify it by using a ROP Gadget to set the registers before jumping to the `system` call. A pop rdi ROP Gadget can be found using `/R pop rdi` in radare2. For the payload, we want it to look as follow:

1. A bunch of garbage to overwrite the stack until we reach the return address
2. The return address (The `pop rdi` gadget in our case)
3. The value we want to pop in `rdi` (the gadget needs to return as soon as possible to avoid rewritting our other registers)
4. The address of the `system` call

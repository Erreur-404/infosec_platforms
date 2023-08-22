Use `nm <executable> | grep ' t '` to get the symbols that are in the text (code) section

> [!INFO]
> From ROP_Emporium:
> "Typically you'll need 40 bytes of garbage to reach the saved return address in the x86_64 binaries, 44 bytes in the x86 binaries and around 36 bytes in the ARMv5 & MIPS binaries."

> [!IMPORTANT]
> gdb debugging with pwntools works with kali

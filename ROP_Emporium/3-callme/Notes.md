## What I the challenge is about:
We need to call the callme_one, callme_two and callme_three methods (from libcallme.so) with the right parameters to decrypt the flag. The parameters can be set with the loc.usefulGadgets symbol (it's the address where we can find the interesting gadgets to set our parameters rdi, rsi and rdx)


Steps:
1. Jump to usefulGadgets (adjust the gadgets), and then to usefulFunction to call the first callme
2. Repeat 2 two more times for the second and last callme
3. Profit

## PLT Notes
The PLT is a data structure that is used to manage function calls between the dynamic linker and the executable program. The PLT is a small code section in the program's address space that contains stub functions, which act as placeholders for the actual functions in the shared libraries. When an external function is called for the first time, the PLT's function stub redirects the call to the dynamic linker which will resolve the address of the actual function and update the PLT with the correct address. Subsequent calls to the external function will go directly to the actual function, bypassing the dynamic linker.

**Here is an example:**

```
0x400720 <callme_one@plt+0> jmp    QWORD PTR [rip+0x20091a]
0x400726 <callme_one@plt+6> push   0x5
0x40072b <callme_one@plt+11> jmp    0x4006c0
0x400730 <setvbuf@plt+0>  jmp    QWORD PTR [rip+0x200912]
0x400736 <setvbuf@plt+6>  push   0x6
0x40073b <setvbuf@plt+11> jmp    0x4006c0
```

What you can se above is the PLT entry for the callme_one function. Any call to the callme_one function from the executable will be directed to `0x400720`. For now, the function hasn't been called yet, so this happens, the program will jump to `[rip+0x20091a]`, which is the following line (`push 0x5`) because the content at `$rip+0x20091a` looks like this: 

```
gef➤ telescope $rip+0x20091a
0x00000000601040│+0x0000: 0x00000000400726  →  <callme_one@plt+6> push 0x5
0x00000000601048│+0x0008: 0x007fd185696e30  →  <setvbuf+0> push r14
0x00000000601050│+0x0010: 0x00000000400746  →  <callme_two@plt+6> push 0x7
0x00000000601058│+0x0018: 0x00000000400756  →  <exit@plt+6> push 0x8
```

You can see that the behavior would have been the same for `setvbuf`. After the push, every entry in the PLT jumps to `0x4006c0`, which corresponds to this:

```
0x4006c0        push   QWORD PTR [rip+0x200942]
0x4006c6        jmp    QWORD PTR [rip+0x200944]
```

These lines make the jump to `dl_runtime_resolve` which is the dynamic linker resolver. After its execution, the actual required function is called and the PLT still looks like this:

```
0x400720 <callme_one@plt+0> jmp    QWORD PTR [rip+0x20091a]        # 0x601040 <callme_one@got.plt>
0x400726 <callme_one@plt+6> push   0x5
0x40072b <callme_one@plt+11> jmp    0x4006c0
```

But the value at `rip+0x20091a` has been modified to jump directly to the actual function:

```
gef➤ telescope $rip+0x20091a
0x0000000060103a│+0x0000: <read@got[plt]+2> jno 0x600fc1
0x00000000601042│+0x0008: <callme_one@got[plt]+2> add BYTE PTR [rbp+0x7fd1], 0x30
0x0000000060104a│+0x0010: <setvbuf@got[plt]+2> imul eax, DWORD PTR [rbp+0x7fd1], 0x400746
```

The table displayed above is the .got.plt table

(not sure why the first value is `read@got[plt]+2` and not `callme_one@got[plt]+2`)


Note to self: I think I can see the PLT as a intermediate between the executable and the shared library. Calls that are directed outside the executable will always go through the PLT, but not always throught the dynamic linker
I think the GOT operates in the same way, but it used for global variables of shared libraries instead of functions


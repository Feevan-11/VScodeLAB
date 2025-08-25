#include "xxx.h"

OUTPUT_ARCH( "riscv" )
ENTRY( _start )

__stack_size = DEFINED(__stack_size) ? __stack_size : 2K;

MEMORY
{
    iram : ORIGIN = 0x04000000, LENGTH = 0x1000
}

SECTIONS
{
    .init           :
    {
        KEEP (*(SORT_NONE(.init)))
    } >iram

    .text           :
    {
        *(.text .text.*)
        *(.gnu.linkonce.t.*)
    } >iram

    .fini           :
    {
        KEEP (*(SORT_NONE(.fini)))
    } >iram

    PROVIDE (__etext = .);
    PROVIDE (_etext = .);
    PROVIDE (etext = .);

    .rodata         :
    {
        *(.rdata)
        *(.rodata .rodata.*)
        *(.gnu.linkonce.r.*)
        . = ALIGN(4);
        PROVIDE( _single_module_start = .);
        KEEP(*(.singletestmodule.*))
        PROVIDE( _single_module_end = . );
        . = ALIGN(4);
        PROVIDE( _test_module_start = .);
        KEEP(*(.testmodule.*))
        PROVIDE( _test_module_end = . );
        . = ALIGN(4);
        PROVIDE( _cli_cmd_start = .);
        KEEP (*(.cli_cmd.*))
        PROVIDE( _cli_cmd_end = .);
    } >iram

    . = ALIGN(4);


    .dtors          :
    {
        KEEP (*crtbegin.o(.dtors))
        KEEP (*crtbegin?.o(.dtors))
        KEEP (*(EXCLUDE_FILE (*crtend.o *crtend?.o ) .dtors))
        KEEP (*(SORT(.dtors.*)))
        KEEP (*(.dtors))
    } >iram

    .data : ALIGN(8)
    {
        *(.data .data.*)
        *(.gnu.linkonce.d.*)
        PROVIDE( _gp = . + 0x800 );
        *(.srodata.cst16)
        *(.srodata.cst8)
        *(.srodata.cst4)
        *(.srodata.cst2)
        *(.srodata .srodata.*)
        *(.sdata .sdata.*)
        *(.gnu.linkonce.s.*)
        . = ALIGN(4);
    } >iram

    PROVIDE( _data_load_addr = LOADADDR(.data) );
    PROVIDE( _data_start = ADDR(.data) );
    PROVIDE( _data_end = ADDR(.data) + SIZEOF(.data) );

    .iram         :
    {
        . = ALIGN(4);
        PROVIDE( _iram_start = . );
        *(.iram.entry*);
        *(.iram*);
        . = ALIGN(4);
        PROVIDE( _iram_end = . );
    } >iram

    .bss : ALIGN(8)
    {
        *(.sbss*)
        *(.gnu.linkonce.sb.*)
        *(.bss .bss.*)
        *(.gnu.linkonce.b.*)
        *(COMMON)
    } >iram

    PROVIDE( _bss_start = ADDR(.bss) );
    PROVIDE( _bss_end = ADDR(.bss) + SIZEOF(.bss) );

    .heap       :
    {
        . = ALIGN(4);
        PROVIDE( _heap_start = . );
        . = ORIGIN(iram) + LENGTH(iram) - __stack_size;
        PROVIDE( _heap_end = . );
    } >iram
    PROVIDE( _heap_size = _heap_end - _heap_start );

    .stack     :
    {
        . += __stack_size;
        PROVIDE( __stack_top = . );
    } >iram
}

#if 0
ASSERT(_heap_size > 0x4000, "Heap size is too small...");
#endif


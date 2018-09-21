# The game starts here.

label start:

    python:
        persistent.oniEnabled = False
        persistent.kokoroClear = False
        persistent.utaguClear = False

    call 01_C from _call_01_C

    if onKokoro:
        call 02_K from _call_02_K
        call 03_K from _call_03_K
        call 04_K from _call_04_K
        call 05_K from _call_05_K
        call 06_K from _call_06_K
        call 07_K from _call_07_K

    if onUtagu:
        call 02_U from _call_02_U
        call 03_U from _call_03_U
        call 04_U from _call_04_U
        call 05_U from _call_05_U
        call 06_U from _call_06_U
        call 07_U from _call_07_U

    if oniEnabled = True:
        call 02_O from _call_02_O
        call 03_O from _call_03_O
        call 04_O from _call_04_O
        call 05_O from _call_05_O
        call 06_O from _call_06_O
        call 07_O from _call_07_O

    return

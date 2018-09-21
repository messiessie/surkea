# The game starts here.

label start:

    python:
        persistent.oniEnabled = False
        persistent.kokoroClear = False
        persistent.utaguClear = False

    call S_01_C from _call_S_01_C

    if onKokoro:
        call S_02_K from _call_S_02_K
        call S_03_K from _call_S_03_K
        call S_04_K from _call_S_04_K
        call S_05_K from _call_S_05_K
        call S_06_K from _call_S_06_K
        call S_07_K from _call_S_07_K

    if onUtagu:
        call S_02_U from _call_S_02_U
        call S_03_U from _call_S_03_U
        call S_04_U from _call_S_04_U
        call S_05_U from _call_S_05_U
        call S_06_U from _call_S_06_U
        call S_07_U from _call_S_07_U

    if oniEnabled = True:
        call S_02_O from _call_S_02_O
        call S_03_O from _call_S_03_O
        call S_04_O from _call_S_04_O
        call S_05_O from _call_S_05_O
        call S_06_O from _call_S_06_O
        call S_07_O from _call_S_07_O

    return

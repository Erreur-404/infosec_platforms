#!/usr/bin/env python

encrypted = '''
PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU.
PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV.

AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V.

EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP.

ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}
'''

dictionnary = {
    'S': 'A',
    'V': 'E',
    'Z': 'D',
    'D': 'H',
    'Q': 'N',
    'P': 'T',
    'N': 'L',
    'O': 'R',
    'F': 'S',
    'A': 'F',
    'U': 'G',
    'R': 'I',
    'L': 'U',
    'G': 'M',
    'X': 'W',
    'B': 'C',
    'E': 'O',
    'M': 'P',
    'I': 'B',
    'H': 'Y',
    'C': 'K',
    'K': 'Q',
    'Y': 'X',
    'J': 'V'
}

decrypted = ''
for i in range(len(encrypted)):
    if encrypted[i].isalpha():
        try:
            decrypted += dictionnary[encrypted[i]]
        except KeyError:
            decrypted += encrypted[i]
    else:
        decrypted += encrypted[i]

print(decrypted)
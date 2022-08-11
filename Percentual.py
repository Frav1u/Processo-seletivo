
from unicodedata import decimal


SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
OUTROS = float(19849.53)

TOTAL = float(SP + RJ + MG + ES + OUTROS)
print(TOTAL)

pSP = ((SP*100)/TOTAL)
pRJ = ((RJ*100)/TOTAL)
pMG = ((MG*100)/TOTAL)
pES = ((ES*100)/TOTAL)
pOUTROS = ((OUTROS*100)/TOTAL)

print('Porcentagem de SP', round(pSP,2),'%')
print('Porcentagem de RJ',  round(pRJ,2),'%')
print('Porcentagem de MG',  round(pMG,2),'%')
print('Porcentagem de ES',  round(pES,2),'%')
print('Porcentagem de OUT', round(pOUTROS,2),'%')
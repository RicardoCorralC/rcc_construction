import RCCpackage.RCCobject as rcco
import sys


if __name__ == '__main__':

	PDB = sys.argv[1]
	CHAIN = sys.argv[2]

	rccs = rcco.RCC(PDB,CHAIN)

	print ','.join(map(str,rccs.RCCvector))




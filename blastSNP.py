f  = file('../Github/PythonHW/prog1.promoter.snp.anchor.out')
records = f.read().split('>')
f.close
f=records[1].strip()  ##""" parse the first alignment only  """
#print f.strip()
aln = f.split('\n\n')
chrom=aln[0].split('\n')[0]
#print aln
for nAlign in range (2,len(aln)):       
    alines=aln[nAlign].split('\n')
    if (len(alines)<3):
        break                       ## This is for the security of the last record.
    line=alines[2]
    subjects=line.split()
    leftCoord=int(subjects[1])
    rightCoord=int(subjects[3])
    nStart=len(subjects[0])+len(subjects[1])+2   ## starting point for alignment, will be problematic if sbject is not longer than query.
    query=alines[0][nStart:]               
    align=alines[1][nStart:]
    subject=alines[2][nStart:]
    for i in range (0,len(subjects[2])):
        if align[i]=="|":
            pass
        else:
            idx=0
            if rightCoord-leftCoord>0:
                idx=i
            else:
                idx=-i
            """
            Being lazy here, does not consier the indel conditions. if indel, count number of "-", subtract it from idx.
            """
            coord=leftCoord+idx
            print chrom,coord,subject[i].upper(),query[i].upper()

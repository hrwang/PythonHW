
####Problem:

1. I can not return and print at the same time in one def?

####Homework:

#####Class code

    class seq:
        def count(self,direc):
            linenum=0
            seqnum=0
            acount=0
            tcount=0
            ccount=0
            gcount=0
            ncount=0
            with open (direc,'r') as f:
                for line in f:
                    linenum+=1
                    if linenum%4==2:
                        seqnum+=1
                        gline=line.strip()
                        for i in range(len(gline)):
                            bp=gline[i]
                            if bp=="A":
                                acount+=1
                            elif bp=="T":
                                tcount+=1
                            elif bp=="C":
                                ccount+=1
                            elif bp=="G":
                                gcount+=1
                            elif bp=="N":
                                ncount+=1
                return acount,tcount,ccount,gcount,ncount,seqnum
        def __init__(self,dire):
            self.dire=dire
            self.a,self.t,self.c,self.g,self.n,self.seqnum=self.count(dire)
        def seq_len(self):
            #print "The total length of nuclotides in this fastq is: ", self.a+self.t+self.c+self.g+self.n
            return self.a+self.t+self.c+self.g+self.n
        def at_content(self):
            return float((self.a+self.t))/float(self.seq_len())
        def cg_content(self):
            return float(self.c+self.g)/float(self.seq_len())
        def report(self):
            length=self.seq_len()
            at=self.at_content()
            cg=self.cg_content()
            ratio=float(at/cg)
            print "The report of ", self.dire,":"
            print "The total length of nuclotides in this fastq is: ", length
            print "The GC content in this fastq is:", "{0:.2f}%".format(cg*100)
            print "The AT in this fastq is:", "{0:.2f}%".format(at*100)
            print "The AT/CG ratio in this fastq is:", "{0:.2f}".format(ratio)
            if cg>0.6:
                print "This is a high GC content organism!\n"
            elif cg>0.4:
                print "This is a moderate GC content organism!\n"
            else:
                print "This is a low GC content organism!\n"

#####Invoking class

    sample_dir="./homework/homework2/data/sample_1.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()
    
    sample_dir="./homework/homework2/data/sample_2.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()
    
    sample_dir="./homework/homework2/data/sample_3.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()
    
    sample_dir="./homework/homework2/data/sample_4.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()
    
    sample_dir="./homework/homework2/data/sample_5.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()
    
    sample_dir="./homework/homework2/data/sample_6.fastq"
    summary_sample=seq(sample_dir)
    summary_sample.report()

#####The report shows up here:

    The report of  ./homework/homework2/data/sample_1.fastq :
    The total length of nuclotides in this fastq is:  27000000
    The GC content in this fastq is: 43.03%
    The AT in this fastq is: 56.90%
    The AT/CG ratio in this fastq is: 1.32
    This is a moderate GC content organism!
    
    The report of  ./homework/homework2/data/sample_2.fastq :
    The total length of nuclotides in this fastq is:  27000000
    The GC content in this fastq is: 45.11%
    The AT in this fastq is: 54.81%
    The AT/CG ratio in this fastq is: 1.22
    This is a moderate GC content organism!
    
    The report of  ./homework/homework2/data/sample_3.fastq :
    The total length of nuclotides in this fastq is:  9510928
    The GC content in this fastq is: 64.69%
    The AT in this fastq is: 35.31%
    The AT/CG ratio in this fastq is: 0.55
    This is a high GC content organism!
    
    The report of  ./homework/homework2/data/sample_4.fastq :
    The total length of nuclotides in this fastq is:  9981008
    The GC content in this fastq is: 34.79%
    The AT in this fastq is: 65.21%
    The AT/CG ratio in this fastq is: 1.87
    This is a low GC content organism!
    
    The report of  ./homework/homework2/data/sample_5.fastq :
    The total length of nuclotides in this fastq is:  76
    The GC content in this fastq is: 26.32%
    The AT in this fastq is: 72.37%
    The AT/CG ratio in this fastq is: 2.75
    This is a low GC content organism!
    
    The report of  ./homework/homework2/data/sample_6.fastq :
    The total length of nuclotides in this fastq is:  27000
    The GC content in this fastq is: 49.15%
    The AT in this fastq is: 50.81%
    The AT/CG ratio in this fastq is: 1.03
    This is a moderate GC content organism!
    



    

bcell_iedb={
    "ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN","S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET","WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
    }

bcell_bepipred={
    "ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN","S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET","WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
    }
# 1. Count the no of epitopes that are common in iedb and bepipred prediction
common_epitopes=(bcell_iedb&bcell_bepipred)
print(common_epitopes)
print(len(common_epitopes))
# 2. Count the no of epiotopes that are present in only iedb b cell prediction
epitopes_iedb=((bcell_iedb|bcell_bepipred)-bcell_bepipred)
print(epitopes_iedb)
print(len(epitopes_iedb))
# 3. Count the no of epiotopes that are present in any of the epitopes but not in both
unique_epitopes=(bcell_bepipred^bcell_iedb)
print(unique_epitopes)
print(len(unique_epitopes))
# Find the total no of uniques epitopes



gc_values=[30.5,12,54,23,84]
n=len(gc_values)
gc_values.sort()

if n % 2 ==0:
    median1=gc_values[n//2]
    median2=gc_values[n//2-1]
    median=gc_values[n//2]
else:
    median=gc_values[n//2]
    print("median is:"+str(median))

import statistics

print("median of gc_values is: %s" %(statistics.median(gc_values)))

# Q2. Write a program to check which stop codons are present in the sequence  â€œUAAAAGGCGAGAUAAAUAâ€
seq1="UAAAAGGCGAGAUAAAUA"
print("UGA" in seq1)
print("UAA" in seq1)
print("UAG" in seq1)

# Check the presence of all the stop codons in the list ["UAA","UGC","AUAGCT","ATUA","UAG"]
listof_stop_codon=["UAA","UGC","AUAGCT","ATUA","UAG"]
for stopcodon in listof_stop_codon:
    if len(stopcodon)<=3:
        print("true")
    else:
        print("false")
        
listof_stop_codon=["UAA","UGC","AUAGCT","ATUA","UAG"]
for stopcodon in listof_stop_codon:
    if len(stopcodon)==3:
        print(stopcodon,len(stopcodon))

# Q5. Concatenate two lists of GC Values [30.5,12,54,23,84] and [12,45,54,32] and find the maxium and minum GC Value

list1=[30.5,12,54,23,84]
list2=[12,45,54,32]
add_both_lists=(list1.__add__(list2))
print(add_both_lists)
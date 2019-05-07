
fi = open("IR_ORF_UP_ALL.tab", "r")

fl = fi.readline()

seen_IR = set()

IR_G = 0
IR_L = 0

for line in fi:
   line = line.rstrip().split("\t")
   cond = line[-3]
   if line[1] not in seen_IR:
      if cond == "True":
         IR_G = IR_G + 1
      elif cond == "False":
         IR_L = IR_L + 1
      seen_IR.add(line[1])

fi.close()

fi = open("all_exonizations_ORF_VYAS.tab", "r")

fl = fi.readline()

seen_EX = set()

EX_G = 0
EX_L = 0

for line in fi:
   line = line.rstrip().split("\t")
   if line[2] not in seen_EX:
      cond = line[-3]
      if cond == "True":
         EX_G = EX_G + 1
      elif cond == "False":
         EX_L = EX_L + 1
      seen_EX.add(line[2])
 
fi.close()

fi = open("all_neoskipping_ORF_FS.tab", "r")

fl = fi.readline()

seen_NS = set()

NS_G = 0
NS_L = 0

for line in fi:
   line = line.rstrip().split("\t")
   if line[3] not in seen_NS:
      cond = line[-3]
      if cond == "True":
         NS_G = NS_G + 1
      elif cond == "False":
         NS_L = NS_L + 1
 
fi.close()

fo = open("percent_barplot_PC.txt", "w")

fo.write("Splicing_event\tPeptide_change\tProportion\n")
fo.write("IR\tTrue\t"+str(IR_G)+"\n")
fo.write("IR\tFalse\t"+str(IR_L)+"\n") 
fo.write("Exonization\tTrue\t"+str(EX_G)+"\n")
fo.write("Exonization\tFalse\t"+str(EX_L)+"\n")
fo.write("Neoskipping\tTrue\t"+str(NS_G)+"\n")
fo.write("Neoskipping\tFalse\t"+str(NS_L)+"\n")


fi = open("IR_Functional_Analysis.txt", "r")

fl = fi.readline()

seen_IR = set()

IR_G = 0
IR_L = 0

for line in fi:
   cond = line.rstrip().split("\t")[1]
   if line not in seen_IR:
      if cond == "Gained":
         IR_G = IR_G + 1
      elif cond == "Lost":
         IR_L = IR_L + 1
      seen_IR.add(line)

fi.close()

fi = open("Exonizations_Functional_Analysis.txt", "r")

fl = fi.readline()

seen_EX = set()

EX_G = 0
EX_L = 0

for line in fi:
   if line not in seen_EX:
      cond = line.rstrip().split("\t")[1]
      if cond == "Gained":
         EX_G = EX_G + 1
      elif cond == "Lost":
         EX_L = EX_L + 1
      seen_EX.add(line)
 
fi.close()

fi = open("Neoskipping_Functional_Analysis.txt", "r")

fl = fi.readline()

seen_NS = set()

NS_G = 0
NS_L = 0

for line in fi:
   if line not in seen_NS:
      cond = line.rstrip().split("\t")[1]
      if cond == "Gained":
         NS_G = NS_G + 1
      elif cond == "Lost":
         NS_L = NS_L + 1
 
fi.close()

fo = open("grouped_barplot_table.txt", "w")

fo.write("Splicing_event\tCondition\tDomains_and_Profiles\n")
fo.write("IR\tGained\t"+str(IR_G)+"\n")
fo.write("IR\tLost\t"+str(IR_L)+"\n") 
fo.write("Exonization\tGained\t"+str(EX_G)+"\n")
fo.write("Exonization\tLost\t"+str(EX_L)+"\n")
fo.write("Neoskipping\tGained\t"+str(NS_G)+"\n")
fo.write("Neoskipping\tLost\t"+str(NS_L)+"\n")

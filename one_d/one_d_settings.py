length=150

first= length//2

rule_N = 90

#computing
bin_rule = bin(rule_N).split('b')[1][::-1]
rule={(1,1,1):0,
      (1,1,0):0,
      (1,0,1):0,
      (1,0,0):0,
      (0,1,1):0,
      (0,1,0):0,
      (0,0,1):0,
      (0,0,0):0,
      }
for iind,i in enumerate(bin_rule):
      for ind,j in enumerate(rule.keys()):
            if ind == iind:
                  rule[j] = int(i)

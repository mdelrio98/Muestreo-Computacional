def run_length_encoding(seq):
    compressed = []
    count = 1
    c= seq[0]
    for i in range(1,len(seq)):
        if seq[i] == c:
            count = count + 1
        else :
            compressed.append([c,count])
            c = seq[i]
            count = 1
    compressed.append([c,count])
    return compressed
 
def run_length_decoding(compressed_seq):
  seq = []
  for i in range(0,len(compressed_seq)):
    rep=compressed_seq[i+1]
    for j in range(rep):
      seq.append(compressed_seq[i])
 
  return(seq)
 
seq = ["5","5","4","5","5","3","3","3","5",
"5","4","4","10","9","5","5","4",
"5","9","10","9","10","10",
"10","2","2","3","14","13","14","13",
"13","2","2","5","13","14","14","4","5"]
list1 = run_length_encoding(seq)
 
compressed_seq = ''
#parsea
for i in range(0,len(list1)):
  for j in list1[i]:
    compressed_seq += str(j)

print("|"+compressed_seq+"|")

list2 = run_length_decoding(list1)
decompressed_seq = ''
#parsea
for i in range(0,len(list2)):
  for j in list2[i]:
    decompressed_seq += str(j)

print("|"+decompressed_seq+"|")
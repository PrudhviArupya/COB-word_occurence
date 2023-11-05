word_cnt={}
file=open('file1.txt','r')
line=file.read().split()
for i in line:
    if i in word_cnt:
        word_cnt[i]+=1
    else:
        word_cnt[i]=1
print("Displaying count of words in a file:")
for i in word_cnt:
    print(i+" - "+str(word_cnt[i]))
print("Displaying unique words in a file:")
l=[i for i in word_cnt if word_cnt[i]==1]
print(l)
    
    

        

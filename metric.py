
tp=573
fp=427
fn=0
    
p=tp/(tp+fp)
print("Precision = ",p)

r=tp/(tp+fn)
print("Recall = ",r)

f=(2*p*r)/(p+r)
print("F1 score = ",f)    


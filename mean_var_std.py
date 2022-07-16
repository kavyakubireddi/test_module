 import numpy as np

def calculate(list):
  if len(list)<9:
   print("List must contain nine numbers.")
  else:
   a=np.reshape(list,(3,3))
  b=(np.mean(a,axis=0),np.mean(a,axis=1),np.mean(a))
  c=(np.var(a,axis=0),np.var(a,axis=1),np.var(a))
  d=(np.std(a,axis=0),np.std(a,axis=1),np.std(a))
  e=(np.max(a,axis=0),np.max(a,axis=1),np.max(a))
  f=(np.min(a,axis=0),np.min(a,axis=1),np.min(a))
  g=(np.sum(a,axis=0),np.sum(a,axis=1),np.sum(a))
  calculations={ 'mean':[b],'variance':[c],'standard deviation':[d],'max':[e],'min':[f],'sum':[g]}
  return calculations
print(calculate([1,2,3,4,5,6,7,8,9]))

import torch as t

def accuracy(y_true, y_pred):
  count = t.eq(y_true, y_pred).sum().item()
  return (count/len(y_true)) * 100

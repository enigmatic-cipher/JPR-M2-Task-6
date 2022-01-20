"""
Given a string as input, print two strings, one of all the chars appearing at odd index and the second of all the chars appearing at even index.
Input-> "A1B2C3D4E"
Output->
Odd:1234
Even:ABCDE
"""

st = "A1B2C3D4E"
ln = len(st)
st1 = ""
st2 = ""
for i in range(0,ln):
  ch = st[i]
  if (i%2==0):
    st1 = st1 + ch
  else:
    st2 = st2 + ch
print("Odd"+":"+st2)
print("Even"+":"+st1)
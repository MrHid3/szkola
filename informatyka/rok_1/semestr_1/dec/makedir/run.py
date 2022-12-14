import os

f = open("data.txt")

for x in f:
    path = x.replace('_', '//')
    path = path.replace('\n', '')
    os.makedirs(path)
    
# dla data.txt
# 1p_grupa1_jkowalski
# 1p_grupa1_okowalska
# 1p_grupa1_anowak
# 1p_grupa2_ekowalska
# 1p_grupa2_jnowak

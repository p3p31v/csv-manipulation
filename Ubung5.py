class cpy:
    def __init__(self,a,b):


            with open(a,'r') as f:
                    with open(b,'w') as f1:
                            for line in f:
                                    f1.write(line)
copy = cpy('Hello.txt', 'Hello_.txt')
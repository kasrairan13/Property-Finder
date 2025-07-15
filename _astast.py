class AbSyTr:
    def __init__(self, proprty, instance_pp):
        self.proprty = proprty
        self.instance_pp = instance_pp
    
    @property
    def proprty(self):
        return self._proprty
    
    @proprty.setter
    def proprty(self, proprty):
        self._proprty = proprty

    @proprty.deleter
    def proprty(self):
        del self._proprty

    
    def get_pp(self):
        return self._pp
    
    def set_pp(self, pp):
        self._pp = pp
    
    def delete_pp(self):
        del self._pp

    
    @property
    def ppppp(self):
        pass
    

    instance_pp = property(get_pp, set_pp, delete_pp)

    instance_pp2 = property()

    xxx = 12


user = AbSyTr("12", 52)
print(user.instance_pp)



for x in (1, 2, 3, 4, 5, 6):
    print(x)

x = list()

x.append(1)
x.append([1, 2, 3, 4, 5])
print(x)

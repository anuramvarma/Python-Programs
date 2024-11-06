class parent: 
    def method1(self): 
        print("Method-1 ") 
class child1(parent): 
    def method2(self): 
        print("Method-2 ") 
class child2(child1): 
    def method3(self): 
        print("Method-3 ") 
obj=child2() 
obj.method1() 
obj.method2() 
obj.method3() 

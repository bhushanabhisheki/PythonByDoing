class A:
  def method_a(self):
    print('Method A of class A')

class B(A):
  def method_b(self):
    print('Method B of class B')

class C(B):
  def method_c(self):
    print('Method C of class C')

obj_c = C()
obj_c.method_a()
obj_c.method_b()
obj_c.method_c()
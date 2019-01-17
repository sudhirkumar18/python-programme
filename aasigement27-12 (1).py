#TODO: list comphresion
#  letters = [letter for letter in 'human']
# print(letters)


# num1 = [4,5,6]
# num2 = [5,6,7]
# result = map(lambda n1,n2:n1+n2,num1,num2)
# print(list(result))

# num = [1, 4, 6, 12, 16, 13]
# result = filter(lambda n1: (n1%2 == 0), num)
# print(list(result))

# letters = list(map(lambda x:x,'sudhir'))
# print(letters)
#
# numers = [x for x in range(50) if x%2 ==0]
# print(numers)

#todo: nested if with list comphresion
numers = [x for x in range(50) if x%2 ==0 if x%5==0 ]
print(numers)


# obj = ["even" if i%2==0 else "odd" for i in range(10)]
# print(obj)


#todo:nested loop in list comphernsion
#
# matrix = [[1, 2],[3, 4],[5, 6],[7, 8]]
# transpose = [[row[i] for row in matrix] for i in range(2)]
# print(transpose)


#todo: dicitonary comphersion


# mydict = {x:x**2 for x in [1,2,3,4,5]}
# print(mydict)


newdict = {x:x**3 for x in range(1,10) if x**3 % 4==0}
print(newdict)

#object__str__(self)
#object__repr__(self)


class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return '(' + str(self.__num) + '/' + str(self.__den) + ')'

    def __repr__(self):
        return 'Fraction (' + str(self.__num) + ',' + str(self.__den) + ')'



f = Fraction(1,2)
print('I want to represent the Fraction STRING as ' + str(f)) # (1/2)
print('I want to represent the Fraction OBJECT as ', repr(f)) # Fraction (1,2)


#object__format__(self,format)

class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print(format(Person(), "age"))

#TODO:ge,ge,gt,lt

class Employee():
    def __init__(self,fname,lname,level,yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    def __ge__(self, other):
        if(self.level == other.level):
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if(self.level == other.level):
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if(self.level == other.level):
            return self.seniority < other.seniority
        return self.level < other.level


    def __eq__(self, other):
        if (self.level == other.level):
            return self.seniority == other.seniority
        return self.level == other.level


    def __le__(self, other):
        if (self.level == other.level):
          return self.seniority <= other.seniority
        return self.level <= other.level

def main():
    # some emplyee
    dept =[]
    dept.append(Employee("parth","shrma" ,2 , 3))
    dept.append(Employee("vinay", "sjain", 3, 2))
    dept.append(Employee("anish", "kumar", 3, 1))
    dept.append(Employee("ravi", "kumar", 2, 3))
    dept.append(Employee("navendu", "shrma", 2, 4))



    emps = sorted(dept)
    print(emps)
    for emp in emps:
        print(emp.fname)
0x09. Python - Everything is object
Task 0: What function would you use to print the type of an object?
Task 1: How do you get the variable identifier (which is the memory address in the CPython implementation)?
Task 2: a = 89 b = 100, do a and b point to the same object?
Task 3: a = 89 b = 89, do a and b point to the same object?
Task 4: a = 89 b = a, do a and b point to the same object?
Task 5: a = 89 b = a + 1, do a and b point to the same object?
Task 6: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 == s2)
Task 7: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = s1 >>> print(s1 is s2)
Task 8: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 == s2)
Task 9: What do these 3 lines print? >>> s1 = "Holberton" >>> s2 = "Holberton" >>> print(s1 is s2)
Task 10: What do these 3 lines print? >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 == l2)
Task 11: What do these 3 lines print? >>> l1 = [1, 2, 3] >>> l2 = [1, 2, 3] >>> print(l1 is l2)
Task 12: What do these 3 lines print? >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 == l2)
Task 13: What do these 3 lines print? >>> l1 = [1, 2, 3] >>> l2 = l1 >>> print(l1 is l2)
Task 14: What does this script print? l1 = [1, 2, 3] l2 = l1 l1.append(4) print(l2)
Task 15: What does this script print? l1 = [1, 2, 3] l2 = l1 l1 = l1 + [4] print(l2)
Task 16: What does this script print? def increment(n): n += 1 a = 1 increment(a) print(a)
Task 17: What does this script print? def increment(n): n.append(4) l = [1, 2, 3] increment(l) print(l)
Task 18: What does this script print? def assign_value(n, v): n = v l1 = [1, 2, 3] l2 = [4, 5, 6] assign_value(l1, l2) print(l1)
Task 19: Write a function def copy_list(l): that returns a copy of a list.
Task 20: a = (), is a a tuple? Answer with Yes or No.
Task 21: a = (1, 2), is a a tuple? Answer with Yes or No.
Task 22: a = (1), is a a tuple? Answer with Yes or No.
Task 23: a = (1, ), is a a tuple? Answer with Yes or No.
Task 24: What does this script print? a = (1) b = (1) a is b
Task 25: What does this script print? a = (1, 2) b = (1, 2) a is b
Task 26: What does this script print? a = () b = () a is b
Task 27: >>> id(a) 139926795932424 >>> a [1, 2, 3, 4] >>> a = a + [5] >>> id(a) Will the last line of this script print 139926795932424? Answer with Yes or No.
Task 28: >>> a [1, 2, 3] >>> id (a) 139926795932424 >>> a += [4] >>> id(a) Will the last line of this script print 139926795932424? Answer with Yes or No.
Task 29: Write a blog post about everything you just learned / this project is covering.
Advanced Task 30: Write a function magic_string() that returns a string “Holberton” n times the number of the iteration.
Advanced Task 31: Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
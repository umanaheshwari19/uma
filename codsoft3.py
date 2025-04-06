#password generator
import random
numbers="123456789"
capital_letter="ABCDEFGHIJKLMN"
small_letter="abcdefghijklmn"
combination=numbers+capital_letter+small_letter
length_Of_password=6
password="".join(random.sample(combination,length_Of_password))
print("The password generator is:",password)


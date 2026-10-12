person_list = []



def count_vowel(person):
    person = person.lower()
    num = 0
    a = person.count("a")
    i = person.count("i")
    e = person.count("e")
    o = person.count("o")
    num = num + a + e + o + i
    return num


while True:
    person = input("enter name")
    if person == "quit":
        break
    person_list.append(person)


person_list.sort(key= count_vowel , reverse=True)

print(person_list)

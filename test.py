import mymodule as test

test.greeting("Brook")


for person in test.people:
    print(person)
    print("Hello my name is "+ person)
    print("I am "+str(test.people[person]["age"])+ " years old")
    print("I am a "+test.people[person]["sign"])
    print("-------------")

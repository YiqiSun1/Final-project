class peopleListLinkedlist: 
    def __init__(self):
        self.head = None
        
    def insert(self, newNode):   #inserting people into linked list
        if self.head is None:
            self.head = newNode
        else:
           lastNode = self.head
           while True:
               if lastNode.next is None:
                   break
               lastNode = lastNode.next
           lastNode.next = newNode
           self.tail = lastNode.next
    
    def get_info(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                return current.age, current.hobbies, current.email, current.phone_number, current.friends
            else:
                current = current.next
            return None

    def match_commonalities(self):
        pass

    def print_people(self):
        currentNode = self.head
        while currentNode is not None:
            currentNode.display()
            currentNode = currentNode.next

class Person: 
    def __init__(self, name, age, hobbies, email, phone_number):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.next = None
        self.email = email
        self.phone_number = phone_number
        self.friends = []


    def match_hobbies(self, people):
        list_of_matching = []
        Target_hobbies = self.hobbies
        list = people
        
        currentNode = list.head
        while True: 
            if currentNode == None:
                break
            if currentNode.hobbies == Target_hobbies:
                list_of_matching.append(currentNode.name)
            currentNode = currentNode.next
        list_of_matching.remove(self.name)
        return list_of_matching

    def be_friends(self, people):
        matches = self.match_hobbies(people)
        print(matches)
        for i in range (0,len(matches)):
            print("You have matched with", matches[i])
            user = input("Match yes or no?")
            if user == "yes":
                self.friend.append(matches[i])
                print("Matched with", matches[i])
            if user == "no":
                print("No match")
        return self.friend
    
    def generates_people(self):
        name = input("Enter your name")
        age = input("Enter your age")
        hobbies = input("Enter your hobbies")
        email = input("Enter your email")
        phone_number = input("Enter your phone number")
        return Person(name, age, hobbies, email, phone_number)

    def display(self):
        print("name:", self.name, "age:", self.age, "hobbies:", self.hobbies, "email:", self.email, "phone number:", self.phone_number, "friends:", self.friend)
        

people = peopleListLinkedlist()
person1 = Person('Kevin', 21, "Golf", "jiangk72@gmail.com", 8582262860)
person2 = Person("Andy", 21, "Golf", "asun25@cmc.edu", 6267026928)
people.insert(person1)
people.insert(person2)
people.print_people()
people.insert()


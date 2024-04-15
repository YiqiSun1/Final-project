class personListLinkedlist: 
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


    def generates_people(self):
        pass
    
    def get_info(self, name):
        pass


    

    def match_commonalities(self):
        pass

class person_node: 
    def __init__(self, name, age, hobbies, email, phone_number):
    
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.next = None
        self.info = email
        self.phone_number = phone_number
        self.friend = []
        
        pass
    
      
    def match_hobbies(self, person_list):
        list_of_matching = []
        Target_hobbies = self.hobbies
        list = person_list
        
        currentNode = list.head
        while True: 
            if currentNode == None:
                break
            if currentNode.hobbies == Target_hobbies:
                list_of_matching.append(currentNode.name)
            currentNode = currentNode.next
        list_of_matching.remove(self.name)
        return list_of_matching
        
    
def wwww

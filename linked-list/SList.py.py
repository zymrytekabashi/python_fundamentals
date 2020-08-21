import SLNode
class SList:
    def __init__(self):
        self.head = None
            
    def add_to_front(self, val):
        new_node = SLNode(val)	# create a new instance of our Node class using the given valueue
        current_head=self.head
        new_node.next = current_head
        self.head = new_node	# SET the list's head TO the node we created in the last step
        return self	                # return self to allow for chaining
    
    def print_values(self):
        runner = self.head	# a pointer to the list's first node
        while (runner != None):	# iterating while runner is a node and not None
            print(runner.value)
            runner=runner.next
        return self
    
    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
        return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self
        
        
my_list= SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!

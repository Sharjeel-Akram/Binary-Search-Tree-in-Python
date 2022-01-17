class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None   
class Binary_Tree:
    def __init__(self):
        self.root = None
        self.flag = False
    def getroot(self):
        return self.root
    def insert_Node(self,node,data):
        if self.root == None:
            self.root = Node(data)
        elif node != None:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    self.insert_Node(node.left, data)
            else:
                if node.right == None:
                    node.right = Node(data)
                else:
                    self.insert_Node(node.right, data)            
    def Search_Node(self,data):
        if self.root:
            Found = self.Search(data,self.root)
            if Found:
                self.flag = True
    def Search(self,data,current_Node):
        if data > current_Node.data and current_Node.right:
            return self.Search(data,current_Node.right)      
        elif data < current_Node.data and current_Node.left:
            return self.Search(data,current_Node.left)
        if data == current_Node.data:
            return True       
    def Height(self,root):
        Height = self.Get_Height(root)
        if Height:
            return Height - 1
    def Get_Height(self,root):
        if root == None:
            return 0
        left_Height = self.Get_Height(root.left)
        right_Height = self.Get_Height(root.right)        
        if left_Height > right_Height:
            return left_Height + 1
        else:
            return right_Height + 1
    def min(self,node):
        if node.left:
            return self.min(node.left)
        return node
    # def Min_value(self):
    #     if self.root:
    #         return self.min(self.root).data
        
    def delete(self,data,node):
        if data < node.data:
            node.left = self.delete(data,node.left)
        elif data > node.data:
            node.right = self.delete(data,node.right)
        else:
            if not node.left:
                temp = node.right
                return temp
            elif not node.right:
                temp = node.left
                return temp
            else:
                temp = self.min(node.right)
                node.data = temp.data
                node.right = self.delete(temp.data,node.right)
        return node
    def Delete_Node(self,data):
        if self.root:
            self.delete(data,self.root)

    def In_Order(self,node):
        if node != None:
            self.In_Order(node.left)
            print(node.data)
            self.In_Order(node.right) 
            return  
    def Pre_Order(self,node):
        if node != None:
            print(node.data)
            self.Pre_Order(node.left)
            self.Pre_Order(node.right)
            return
    def Post_Order(self,node):
        if node != None:
            self.Post_Order(node.left)
            self.Post_Order(node.right)
            print(node.data)
            return
    # def Display(self):
    #     Do = input("Please Press S to start the program: ")
    #     BST = Binary_Tree()
    #     while Do != "h":
    #         choice = input("pleased enter your choice from a,b,c,d,e,f,g,s,h: ") 
    #         if choice == "a":
    #             loop = input("enter how many time you want to insert node: ")
    #             for i in range(int(loop)):
    #                 N = int(input("please enter the value for node: "))
    #                 BST.insert_Node(BST.root,N)
    #             print("In_Order Values")
    #             BST.In_Order(BST.getroot())
    #             print("Pre_Order Values")
    #             BST.Pre_Order(BST.getroot())
    #             print("Post_Order Values")
    #             BST.Post_Order(BST.getroot())
    #         elif choice == "b":
    #             Node = int(input("enter the node which you want to seach in tree: "))
    #             BST.Search_Node(Node)
    #             if(BST.flag):  
    #                 print("Node exists in the binary tree")  
    #             else:  
    #                 print("Node does not exist in the binary tree") 
    #         elif choice == "c":
    #             Value = int(input("Enter the node which you want to delete from Binary tree: "))
    #             BST.Delete_Node(Value)
    #             print("In_Order Values")
    #             BST.In_Order(BST.getroot())
    #             print("Pre_Order Values")
    #             BST.Pre_Order(BST.getroot())
    #             print("Post_Order Values")
    #             BST.Post_Order(BST.getroot())
    #         elif choice == "d":
    #             print("Pre_Order Values")
    #             BST.Pre_Order(BST.getroot())
    #         elif choice == "e":
    #             print("In_Order Values")
    #             BST.In_Order(BST.getroot())
    #         elif choice == "f":
    #             print("Post_Order Values")
    #             BST.Post_Order(BST.getroot())   
    #         elif choice == "g":
    #             print("The Height of BST is: ",BST.Height(BST.root))
    #         elif choice == "h":
    #             break
BST = Binary_Tree()
BST.insert_Node(BST.root,10)
BST.insert_Node(BST.root,5)
BST.insert_Node(BST.root,12)
BST.insert_Node(BST.root,11)
# BST.insert_Node(BST.root,5)
# BST.insert_Node(BST.root,7)
# BST.insert_Node(BST.root,65)
# BST.insert_Node(BST.root,15)
# BST.insert_Node(BST.root,4)
# BST.insert_Node(BST.root,9)
# BST.insert_Node(BST.root,48)
# BST.Display()
BST.Pre_Order(BST.root)
BST.Delete_Node(10)
print("Delete")
BST.Pre_Order(BST.root)
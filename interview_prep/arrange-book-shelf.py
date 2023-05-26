'''
There are books in a shelf, Either type of X or Y, Your mom 
wants to make sure before your birthday party, shelf is arranged. 
All the X type of books should be on left, and all the books of 
type Y should be on right. There is a time cost associated with each swap, 
output if it is possible to arrange them before the party starts.
'''

def arrange(books):
    '''
        Solving by two pointers method in order of O(N)
        N - number of books
    '''
    head = 0
    tail = len(books)-1

    while head != tail:
        if books[head] == 'X':
            head += 1
        
        else:
            if books[tail] == 'Y':
                tail -= 1
            
            else:
                books[head], books[tail] = 'X','Y'

books = ['Y','Y','X','Y','X']
arrange(books)
print(books)

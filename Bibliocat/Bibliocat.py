class Library:
    
    def __init__(self, id):
        self.id = id
        self.transport_time = dict()

    def add_transport_time(self, id_to, time):
        self.transport_time[id_to] = time

class Reader:
    
    def __init__(self, id, library_id):
        self.id = id
        self.library_id = library_id
        self.lecture_time = dict()
        
    def add_lecture_time(self, id_book, time):
        self.lecture_time[id_book] = time


class Book:
    def __init__(self, id, value, library_id):
        self.id = id
        self.value = value
        self.library_id = library_id

def parse_initial_data():
    time = 0
    libraries = dict()
    books = dict()
    readers = dict()

    with open("input_file.txt") as f:
        for line in f:
            selector = line[0]
            if selector == 'T':
                time = line.split(' ')[1]

            elif selector == 'L':
                _line = line.split(' ')
                library = Library(int(_line[1]))
                count = 0
                for i in range(2, len(_line)):
                    library.transport_time[count] = int(_line[i])
                    count += 1      
                libraries[library.id] = library

            elif selector == 'B':
                _line = line.split(' ')
                book = Book(int(_line[1]), int(_line[2]), int(_line[3]))
                books[book.id] = book

            elif selector == 'R':
                _line = line.split(' ')
                reader = Reader(int(_line[1]), int(_line[2]))
                for i in range(3, len(_line), 2):
                    reader.add_lecture_time(int(_line[i]), int(_line[i+1]))
                readers[reader.id] = reader  
                
    return int(time), libraries, books, readers

if __name__ == "__main__":

    time, libraries, books, readers = parse_initial_data()

    


    


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self, name, age):
        print('안녕하세요! 제 이름은 {}, {}살 입니다!'.format(self.name, self.age))
        
        
class Book:
    def __init__(self, name, librarian):
        self.name = name
        self.librarian = librarian


class Librarian(Person):
    def __init__(self, name, age, book=list()):
        super().__init__(name, age) # 상위 클래스 상속
        self.__book = book

    def add_book(self, new_book): #새책을 받거나, 반납받는 함수
        self.__book.append(new_book)        
        
        
    def remove_book(self, removed_book): #책을 빌려주는 함수
        self.__book.remove(removed_book)
        return self.__book
        
        
    def get_book_list(self): #관리중인 책 목록을 반환하는 함수    
        return self.__book
        

class User(Person):
    def __init__(self, name, age, book_list=list()):
        super().__init__(name, age)
        self.book__list = book_list

    def borrow_book(self, new_book): #책을 대출하는 함수 
        self.book__list.append(new_book)
        
        
    def return_book(self, return_book): #책을 반납하는 함수
        self.book__list.remove(return_book)
        if self.book__list == []:
            return True
        return self.book__list
        

    def get_borrowed_list(self):  #빌린 책 목록을 반환하는 함수  
        return self.book__list
        
a = 

gdgdg
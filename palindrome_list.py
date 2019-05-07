from stack import StackDynamicArray


def is_palindrom(word):
    '''
    Checks whether the word is a palindrome.
    :param word: str
    :return: bool
    '''
    stack1 = StackDynamicArray()
    stack2 = StackDynamicArray()
    for el in word[:len(word) // 2]:
        stack1.push(el)
    if len(word) % 2:
        for letter in word[((len(word) // 2) + 1):][::-1]:
            stack2.push(letter)
    else:
        for letter in word[(len(word) // 2):][::-1]:
            stack2.push(letter)
    for i in range(len(stack1)):
        if stack1.peek() == stack2.peek():
            stack1.pop()
            stack2.pop()
    if stack1.isEmpty() and stack2.isEmpty():
        return True
    else:
        return False


class Palindrom:
    def read_from_file(self, filename):
        '''
        Reads the dictionary from a file named filename
        :param filename: str
        :return: None
        '''
        inf = []
        file = open(filename, "r", encoding="utf8")
        data = file.read().split("\n")
        for exp in data:
            if exp:
                if exp[0].isalpha():
                    inf.append(exp.split()[0])
        self.data = inf
        file.close()

    def check_the_dictionary(self):
        '''
        Checks which of the words in the dictionary are palindromes and saves them into a string.
        :return: str
        '''
        text = ""
        for el in self.data:
            if is_palindrom(el):
                text += el + "\n"
        return text

    def write(self, filename):
        '''
        Writes all the palindromes to the file named filename
        :param filename: str
        :return: None
        '''
        with open(filename, "w+", encoding="utf-8") as f:
            text = self.check_the_dictionary()
            print(text)
            f.write(text)


p1 = Palindrom()
p1.read_from_file("base.lst")
p1.write("palindrome_uk.txt")
p2 = Palindrom()
p2.read_from_file("words.txt")
p2.write("palindrome_en.txt")

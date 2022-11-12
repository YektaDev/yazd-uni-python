# __iter__
# __next__

class Employee():
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.workdays = ['mondary', 'tuesday']

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f'Name: {self.name}, Tasks: {self.tasks}'

    def __getitem__(self, idx):
        return self.workdays[idx]

    def __iter__(self):
        self.n = 0  # initialization
        return self

    def __next__(self):
        if self.n < len(self.tasks):
            t = self.tasks[self.n]
            self.n += 1
            return t
        else:
            raise StopIteration


e1 = Employee('Ali')
e1.add_task('Task 1')
e1.add_task('Project 12')
print(e1)

for t in e1:
    print(t)

print(e1[0])


# ====================================================== Exercise ======================================================
class Book():
    def __init__(self, authors, title, year, chapters):
        self.authors = authors
        self.title = title
        self.year = year
        self.chapters = chapters

    def __str__(self):
        return f'"{self.title}" by {self.authors} ({self.year})'

    def __getitem__(self, idx):
        return self.authors[idx]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.chapters):
            c = self.chapters[self.n]
            self.n += 1
            return c
        else:
            raise StopIteration


book1 = Book(['Ali', 'Majid'], 'Python is technically worse than Kotlin by a far margin!', 2018,
             ['list', 'tuples', 'dict'])

for chapter in book1:
    print(chapter)

print(book1[0])
print(book1[1])

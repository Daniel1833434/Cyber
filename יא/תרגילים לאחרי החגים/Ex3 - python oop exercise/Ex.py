import datetime
class Note:
    def __init__(self,**Data):
        self.content = Data["content"] if "content" in Data else ''
        if "creation_time" in Data:
            self.creation_time = Data["creation_time"]
        else:
            self.creation_time =datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    def find_in_content(self,word):
        return word in self.content

class NoteBook(Note):
    def __init__(self,**Data):
        self.notes =[]
        content = Data["content"] if "content" in Data else ''
        notes_file = Data["notes_file"] if "notes_file" in Data else ''
        if "content" in Data:
            self.notes.append(Note(content = content))
        if notes_file != '':
            with open(notes_file,"r") as file:
                for note in file:
                    noteContent = note.split('$')[1]
                    noteTime = note.split('$')[2].strip()
                    self.notes.append(Note(content= noteContent , creation_time= noteTime))

    def add_note(self,content):
        self.notes.append(Note(content=content))

    def sort_notes(self,**Data):
        up_Down = Data['updown'] if "updown" in Data else 'up'
        return sorted(self.notes,key = lambda note : datetime.datetime.strptime(note.creation_time,"%d-%m-%y %H:%M:%S"),reverse = up_Down == 'down')

    def print_notes_contained(self,word):
        for note in self.notes:
            if note.find_in_content(word):
                print(note.content + " " + note.creation_time)

    def find_in_notes(self,word):#לא הבנתי למה צריך לכתוב את אותה פונקציה פעמיים
        for note in self.notes:
            if note.find_in_content(word):
                print(note.content + " " + note.creation_time)

    def __str__(self):
        ret=''
        for note in self.notes:
            ret += note.content +" "+ note.creation_time + '\n'
        return ret

if __name__ == '__main__':
    nb1 = NoteBook(notes_file='notes_file.txt', content='adding my first note')
    nb2 = NoteBook()
    nb1.add_note('adding my second note')
    nb1.add_note('adding my third note')
    nb2.add_note('note 1 at nb2')
    nb2.add_note('note 2 at nb2')
    print('prints all notes at nb1')
    print(nb1)
    print()
    print('prints all notes at nb2')
    print(nb2)
    print()
    print('Print all note contains python')
    nb1.print_notes_contained('python')
    print()
    print('Sorted notes at nb1 - up')
    nb1.notes= nb1.sort_notes(updown='up')
    print(nb1)
    print()
    print('Sorted notes at nb1 - down')
    nb1.notes = nb1.sort_notes(updown='down')
    print(nb1)


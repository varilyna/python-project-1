from tkinter import Text, WORD, BOTH, LEFT, Y, Scrollbar

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.textarea, self.scroll = self.create_text_area()

    def create_text_area(self):
        text_field = Text(self.root,
                          padx=10,
                          pady=10,
                          wrap=WORD,
                          spacing3=10,
                          width=30,
                          font='Arial 14 bold'
                          )
        text_field.pack(expand=1, fill=BOTH, side=LEFT)

        scroll = Scrollbar(self.root, command=text_field.yview)
        scroll.pack(side=LEFT, fill=Y)
        text_field.config(yscrollcommand=scroll.set)

        return text_field, scroll

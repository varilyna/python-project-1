from tkinter import END
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

class Menu1:
    def __init__(self, root, text_field):
        self.root = root
        self.text_field = text_field

    def open_file(self):
        file_path = filedialog.askopenfilename(title='Выбор файла',
                                               filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            self.text_field.delete('1.0', END)
            self.text_field.insert('1.0', open(file_path, encoding='utf-8').read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                text = self.text_field.get('1.0', END)
                f.write(text)

    def exit(self):
        answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
        if answer:
            self.root.destroy()

    def search_text(self):
        search_text = simpledialog.askstring("Найти", "Введите слово для поиска:")
        if search_text:
            start_pos = '1.0'
            while True:
                start_pos = self.text_field.search(search_text, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(search_text)}c'
                self.text_field.tag_add('found', start_pos, end_pos)
                start_pos = end_pos
            self.text_field.tag_config('found', background='pink')

    def replace_text(self):
        search_text = simpledialog.askstring("Найти", "Введите слово для поиска:")
        if search_text:
            replace_text = simpledialog.askstring("Заменить", f"Введите слово для замены '{search_text}' на:")
            if replace_text:
                content = self.text_field.get('1.0', END)
                new_content = content.replace(search_text, replace_text)
                self.text_field.delete('1.0', END)
                self.text_field.insert('1.0', new_content)

from tkinter import Tk, Menu
from src import View, Menu1, TextEditor

root = Tk()
root.title('Текстовый редактор')
root.geometry('600x700')
root.iconbitmap('Unknown.png')

main_menu = Menu(root)

# Create TextEditor instance
text_editor = TextEditor(root)

# View
view = View(text_editor.textarea)
menu1 = Menu1(root, text_editor.textarea)

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=menu1.open_file)
file_menu.add_command(label='Сохранить', command=menu1.save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=menu1.exit)
root.config(menu=file_menu)

view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: view.change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: view.change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: view.change_font('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: view.change_font('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: view.change_font('TNR'))
font_menu_sub.add_command(label='Verdana', command=lambda: view.change_font('Verdana'))
font_menu_sub.add_command(label='Helvetica', command=lambda: view.change_font('Helvetica'))
font_menu_sub.add_command(label='Tahoma', command=lambda: view.change_font('Tahoma'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

text_menu = Menu(main_menu, tearoff=0)
text_menu.add_command(label='Найти', command=menu1.search_text)
text_menu.add_command(label='Заменить', command=menu1.replace_text)
root.config(menu=text_menu)


# Add menu items
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
main_menu.add_cascade(label='Найти/Заменить', menu=text_menu)
root.config(menu=main_menu)

root.mainloop()

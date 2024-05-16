class View:
    def __init__(self, text_field):
        self.view_colors = {
            'dark': {
                'text_bg': 'black', 'text_fg': 'white', 'cursor': 'pink', 'select_bg': '#8D917A'
            },
            'light': {
                'text_bg': 'white', 'text_fg': 'black', 'cursor': 'pink', 'select_bg': '#FAEEDD'
            }
        }

        self.fonts = {
            'Arial': {
                'font': 'Arial 14 bold'
            },
            'CSMS': {
                'font': ('Comic Sans MS', 14, 'bold')
            },
            'TNR': {
                'font': ('Times New Roman', 14, 'bold')
            },
            'Verdana' : {
                'font': ('Verdana', 14, 'bold')
            },
            'Helvetica': {
                'font': ('Helvetica', 14, 'bold')
            },
            'Tahoma': {
                'font': ('Tahoma', 14, 'bold')
            }
        }
        self.text_field = text_field
        self.view_colors = self.view_colors
        self.fonts = self.fonts
        self.theme = 'light'
        self.font = 'Arial 14 bold'


    def change_theme(self, theme):
        self.theme = theme
        colors = self.view_colors[theme]
        self.text_field.configure(bg=colors['text_bg'], fg=colors['text_fg'], insertbackground=colors['cursor'],
                                  selectbackground=colors['select_bg'])

    def change_font(self, font):
        self.font = self.fonts[font]['font']
        self.text_field.configure(font=self.font)

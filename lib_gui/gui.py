from tkinter import Tk, Frame, Button, Label, Entry, messagebox, StringVar, BOTH
from tkinter.ttk import Combobox

from .codificadores import *
from .decodificadores import *


def gui() -> None:
    """Função principal da interface gráfica"""

    def iniciar(_) -> None:
        """Função para iniciar o segundo frame"""

        def voltar() -> None:
            """Função para voltar ao menu principal"""
            cbx1.set('')
            cbx2.set('')

            root.geometry('300x170')
            root.title('Menu principal')
            frame2.destroy()
            frame1.pack(expand=True, fill=BOTH)

        def gerar_resultado() -> None:
            """Função para gerar o resultado"""

            try:
                if cbx2.current() in (0, 2, 4, 5):
                    res.set(cifra(ent_msg.get(), ent_cha.get()))
                elif cbx2.current() == 1:
                    res.set(cifra(ent_msg.get()))
                elif cbx2.current() == 3:
                    res.set(cifra(ent_msg.get(), cbx_esc.current()))

            except ValueError:
                messagebox.showerror('ValueError', 'Chave passada é inválida.')

        if cbx1.get():
            # Colocando na variável cifra uma função de acordo com as escolhas do usuário
            if cbx1.get() == 'Codificar':
                cifra = [cod_cesar, cod_morse, cod_onetimepad, cod_tapcode,
                         cod_vigenere, cod_autokey][cbx2.current()]
            elif cbx1.get() == 'Decodificar':
                cifra = [decod_cesar, decod_morse, decod_onetimepad, decod_tapcode,
                         decod_vigenere, decod_autokey][cbx2.current()]

            # Escondendo o menu principal e mostrando a opção do usuário
            root.geometry('350x200')
            frame1.pack_forget()

            # Criando o segundo frame
            frame2 = Frame(root, bg='#252422')
            frame2.pack(expand=True, fill=BOTH)

            # Mudando o nome da janela para a opção do usuário
            root.title(cbx1.get() + ' ' + cbx2.get().lower())

            # Colocando os widgets essenciais na janela
            lbl_msg = Label(frame2, text='Mensagem', bg='#fffcf2')
            lbl_msg.grid(column=0, row=0, sticky='W', padx=10, pady=8)

            ent_msg = Entry(frame2, width=55)
            ent_msg.grid(column=0, row=1, sticky='W', padx=10, pady=8)

            lbl_res = Label(frame2, text='Resultado', bg='#fffcf2')
            lbl_res.grid(column=0, row=4, sticky='W', padx=10, pady=16)

            res = StringVar()
            ent_res = Entry(frame2, width=55, state='readonly', textvariable=res)
            ent_res.grid(column=0, row=5, sticky='W', padx=10, pady=0)

            bnt_voltar = Button(frame2, text='Voltar', bg='#eb5e28')
            bnt_voltar['command'] = voltar
            bnt_voltar.grid(column=0, row=6, sticky='W', padx=10, pady=16)

            bnt_res = Button(frame2, text='Gerar resultado', bg='#ccc5b9', activebackground='#ccc5b9')
            bnt_res['command'] = gerar_resultado
            bnt_res.grid(column=0, row=6, padx=10)

            if cbx2.current() in (0, 2, 4, 5):
                # Colocando os widgets de chave
                root.geometry('350x270')
                lbl_cha = Label(frame2, text='Chave', bg='#fffcf2')
                lbl_cha.grid(column=0, row=2, sticky='W', padx=10, pady=16)

                ent_cha = Entry(frame2, width=55)
                ent_cha.grid(column=0, row=3, sticky='W', padx=10, pady=0)

            elif cbx2.current() == 3:
                # Colocando os widgets de escolha
                root.geometry('350x270')
                lbl_esc = Label(frame2, text='Modo de codificação', bg='#fffcf2')
                lbl_esc.grid(column=0, row=2, sticky='W', padx=10, pady=16)

                cbx_esc = Combobox(frame2, state='readonly')
                cbx_esc.config(values=('Por pares de números', 'Por pontos'))
                cbx_esc.grid(column=0, row=3, sticky='W', padx=10, pady=0)

    root = Tk()
    root.title('Menu principal')
    root.geometry('300x170')
    root.resizable(width=False, height=False)

    # Frame1
    frame1 = Frame(root, bg='#252422')
    frame1.pack(expand=True, fill=BOTH)

    cbx1 = Combobox(frame1, values=('Codificar', 'Decodificar'), state='readonly')
    cbx1.grid(column=0, row=1, padx=10, pady=8)

    cbx2 = Combobox(frame1, state='readonly')
    cbx2.config(values=('Cifra de César', 'Código morse', 'One-time pad',
                        'Tap code', 'Cifra de Vigenère', 'Autokey cipher'))
    cbx2.grid(column=0, row=3, padx=10)
    cbx2.bind("<<ComboboxSelected>>", iniciar)

    lbl1 = Label(frame1, text='Operação', bg='#fffcf2')
    lbl1.grid(column=0, row=0, sticky='W', padx=10, pady=8)

    lbl2 = Label(frame1, text='Codificação', bg='#fffcf2')
    lbl2.grid(column=0, row=2, sticky='W', padx=10, pady=16)

    root.mainloop()

from tkinter import Tk, Frame, Button, Label, Entry, messagebox, StringVar, BOTH
from tkinter.ttk import Combobox

from .codificadores import cod_cesar, cod_vigenere, cod_onetimepad, cod_morse, cod_tapcode, cod_autokey, cod_niilista
from .decodificadores import decod_cesar, decod_vigenere, decod_onetimepad, decod_morse, decod_tapcode, decod_autokey, decod_niilista


def gui() -> None:
    """Função principal da interface gráfica"""

    def iniciar(_) -> None:
        """Função para iniciar o segundo frame"""

        def voltar() -> None:
            """Função para voltar ao menu principal"""
            cbx_ope.set('')
            cbx_cript.set('')

            root.geometry('300x170')
            root.title('Menu principal')
            frame_opc.destroy()
            frame_menu.pack(expand=True, fill=BOTH)

        def gerar_resultado() -> None:
            """Função para gerar o resultado"""

            try:
                if cbx_cript.current() in (0, 2, 4, 5):
                    res.set(cifra(ent_msg.get(), ent_cha.get()))
                elif cbx_cript.current() == 1:
                    res.set(cifra(ent_msg.get()))
                elif cbx_cript.current() == 3:
                    res.set(cifra(ent_msg.get(), cbx_esc.current()))
                elif cbx_cript.current() == 6:
                    res.set(cifra(ent_msg.get(), ent_pala.get(), ent_cha.get()))
            except ValueError:
                messagebox.showerror('ValueError', 'Chave passada é inválida.')

        if cbx_ope.get():
            # Colocando na variável cifra uma função de acordo com as escolhas do usuário
            if cbx_ope.get() == 'Codificar':
                cifra = [cod_cesar, cod_morse, cod_onetimepad, cod_tapcode,
                         cod_vigenere, cod_autokey, cod_niilista][cbx_cript.current()]
            elif cbx_ope.get() == 'Decodificar':
                cifra = [decod_cesar, decod_morse, decod_onetimepad, decod_tapcode,
                         decod_vigenere, decod_autokey, decod_niilista][cbx_cript.current()]

            # Escondendo o menu principal e mostrando a opção do usuário
            root.geometry('350x200')
            frame_menu.pack_forget()

            # Frame da opção do usuário
            frame_opc = Frame(root, bg='#252422')
            frame_opc.pack(expand=True, fill=BOTH)

            # Mudando o nome da janela para a opção do usuário
            root.title(cbx_ope.get() + ' ' + cbx_cript.get().lower())

            # Colocando os widgets essenciais na janela
            lbl_msg = Label(frame_opc, text='Mensagem', bg='#fffcf2')
            lbl_msg.grid(column=0, row=0, sticky='W', padx=10, pady=8)

            ent_msg = Entry(frame_opc, width=55)
            ent_msg.grid(column=0, row=1, sticky='W', padx=10, pady=8)

            lbl_res = Label(frame_opc, text='Resultado', bg='#fffcf2')
            lbl_res.grid(column=0, row=6, sticky='W', padx=10, pady=16)

            res = StringVar()
            ent_res = Entry(frame_opc, width=55, state='readonly', textvariable=res)
            ent_res.grid(column=0, row=7, sticky='W', padx=10, pady=0)

            bnt_voltar = Button(frame_opc, text='Voltar', bg='#eb5e28')
            bnt_voltar['command'] = voltar
            bnt_voltar.grid(column=0, row=8, sticky='W', padx=10, pady=16)

            bnt_res = Button(frame_opc, text='Gerar resultado', bg='#ccc5b9', activebackground='#ccc5b9')
            bnt_res['command'] = gerar_resultado
            bnt_res.grid(column=0, row=8, padx=10)

            if cbx_cript.current() in (0, 2, 4, 5):
                # Colocando os widgets de chave
                root.geometry('350x270')
                lbl_cha = Label(frame_opc, text='Chave', bg='#fffcf2')
                lbl_cha.grid(column=0, row=2, sticky='W', padx=10, pady=16)

                ent_cha = Entry(frame_opc, width=55)
                ent_cha.grid(column=0, row=3, sticky='W', padx=10, pady=0)

            elif cbx_cript.current() == 3:
                # Colocando os widgets de escolha
                root.geometry('350x270')
                lbl_esc = Label(frame_opc, text='Modo de codificação', bg='#fffcf2')
                lbl_esc.grid(column=0, row=2, sticky='W', padx=10, pady=16)

                cbx_esc = Combobox(frame_opc, state='readonly')
                cbx_esc.config(values=('Por pares de números', 'Por pontos'))
                cbx_esc.grid(column=0, row=3, sticky='W', padx=10, pady=0)
            
            elif cbx_cript.current() == 6:
                # Colocando os widgets de chave e palavra-chave
                root.geometry('350x340')
                lbl_pala = Label(frame_opc, text='Palavra-chave', bg='#fffcf2')
                lbl_pala.grid(column=0, row=2, sticky='W', padx=10, pady=16)
                ent_pala = Entry(frame_opc, width=55)
                ent_pala.grid(column=0, row=3, sticky='W', padx=10, pady=0)

                lbl_cha = Label(frame_opc, text='Chave', bg='#fffcf2')
                lbl_cha.grid(column=0, row=4, sticky='W', padx=10, pady=16)

                ent_cha = Entry(frame_opc, width=55)
                ent_cha.grid(column=0, row=5, sticky='W', padx=10, pady=0)

    root = Tk()
    root.title('Menu principal')
    root.geometry('300x170')
    root.resizable(width=False, height=False)

    # Frame do menu
    frame_menu = Frame(root, bg='#252422')
    frame_menu.pack(expand=True, fill=BOTH)

    cbx_ope = Combobox(frame_menu, values=('Codificar', 'Decodificar'), state='readonly')
    cbx_ope.grid(column=0, row=1, padx=10, pady=8)

    cbx_cript = Combobox(frame_menu, state='readonly')
    cbx_cript.config(values=('Cifra de César', 'Código morse', 'One-time pad',
                        'Tap code', 'Cifra de Vigenère', 'Autokey cipher',
                         'Cifra niilista'))
    cbx_cript.grid(column=0, row=3, padx=10)
    cbx_cript.bind("<<ComboboxSelected>>", iniciar)

    lbl_ope = Label(frame_menu, text='Operação', bg='#fffcf2')
    lbl_ope.grid(column=0, row=0, sticky='W', padx=10, pady=8)

    lbl_cript = Label(frame_menu, text='Criptografia', bg='#fffcf2')
    lbl_cript.grid(column=0, row=2, sticky='W', padx=10, pady=16)

    root.mainloop()

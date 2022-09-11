import tkinter as tk
import os, sys
from PIL import ImageTk, Image
from scripts import resistencia_equivalente_serie, resistencia_equivalente_paralelo,\
    resistencia_equivalente_paralelo_jre, corriente_total, potencia_total, multiplicacion, division


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


bgclr = "#6576B4"
icon = resource_path("tkalc.ico")
rspng = resource_path("resistances_serie.png")
rppng = resource_path("resistances_paralelo.png")
rpjpng = resource_path("resistances_paralelo_jre.png")


def result_button(f, v, r1, r2, r3):
    k = 0
    try:
        if f == 1:
            tmp_r_e = resistencia_equivalente_serie(r1, r2, r3)

            tmp_i_t = division(v, tmp_r_e)
            tmp_i_1 = tmp_i_t
            tmp_i_2 = tmp_i_t
            tmp_i_3 = tmp_i_t
            tmp_v_1 = multiplicacion(r1, tmp_i_1)
            tmp_v_2 = multiplicacion(r2, tmp_i_2)
            tmp_v_3 = multiplicacion(r3, tmp_i_3)
            tmp_p_t = multiplicacion(v, tmp_i_t)
            tmp_p_1 = multiplicacion(tmp_v_1, tmp_i_1)
            tmp_p_2 = multiplicacion(tmp_v_2, tmp_i_2)
            tmp_p_3 = multiplicacion(tmp_v_3, tmp_i_3)

        elif f == 2:
            tmp_r_e = resistencia_equivalente_paralelo(r1, r2, r3)
            tmp_v_1 = v
            tmp_v_2 = v
            tmp_v_3 = v
            tmp_i_t = division(v, tmp_r_e)
            tmp_i_1 = division(tmp_v_1, r1)
            tmp_i_2 = division(tmp_v_2, r2)
            tmp_i_3 = division(tmp_v_3, r3)
            tmp_p_t = multiplicacion(v, tmp_i_t)
            tmp_p_1 = multiplicacion(tmp_v_1, tmp_i_1)
            tmp_p_2 = multiplicacion(tmp_v_2, tmp_i_2)
            tmp_p_3 = multiplicacion(tmp_v_3, tmp_i_3)

        elif f == 3:
            tmp_r_e = resistencia_equivalente_paralelo_jre(r1, r2)

        else:
            print("error")

    finally:

        clear_widgets(rwframe)
        try:
            if f == 1 or f == 2:
                r_e = float("{:.3f}".format(float(tmp_r_e)))
                v_1 = float("{:.3f}".format(float(tmp_v_1)))
                v_2 = float("{:.3f}".format(float(tmp_v_2)))
                v_3 = float("{:.3f}".format(float(tmp_v_3)))
                i_t = float("{:.3f}".format(float(tmp_i_t)))
                i_1 = float("{:.3f}".format(float(tmp_i_1)))
                i_2 = float("{:.3f}".format(float(tmp_i_2)))
                i_3 = float("{:.3f}".format(float(tmp_i_3)))
                p_t = float("{:.3f}".format(float(tmp_p_t)))
                p_1 = float("{:.3f}".format(float(tmp_p_1)))
                p_2 = float("{:.3f}".format(float(tmp_p_2)))
                p_3 = float("{:.3f}".format(float(tmp_p_3)))
                k = 1
            elif f == 3:
                r_e = float("{:.3f}".format(float(tmp_r_e)))
                k = 1

        except:
            if f == 1 or f == 2:
                r_e = tmp_r_e
                v_1 = tmp_v_1
                v_2 = tmp_v_2
                v_3 = tmp_v_3
                i_t = tmp_i_t
                i_1 = tmp_i_1
                i_2 = tmp_i_2
                i_3 = tmp_i_3
                p_t = tmp_p_t
                p_1 = tmp_p_1
                p_2 = tmp_p_2
                p_3 = tmp_p_3
                k = 2
            elif f == 3:
                r_e = tmp_r_e
                k = 2

        finally:
            if k == 1:
                if f == 1 or f == 2:
                    tk.Label(
                        rwframe,
                        text=f"Resistencia Equivalente: {r_e} Ω\n"
                             f"\nVoltaje Resistencia 1: {v_1} V\n"
                             f"\nVoltaje Resistencia 2: {v_2} V\n"
                             f"\nVoltaje Resistencia 3: {v_3} V\n"
                             f"\nCorriente Total: {i_t} A\n"
                             f"\nCorriente Resistencia 1: {i_1} A\n"
                             f"\nCorriente Resistencia 2: {i_2} A\n"
                             f"\nCorriente Resistencia 3: {i_3} A\n"
                             f"\nPotencia Total: {p_t}\n"
                             f"\nPotencia Resistencia 1: {p_1}\n"
                             f"\nPotencia Resistencia 2: {p_2}\n"
                             f"\nPotencia Resistencia 3: {p_3}",
                        bg="#2A3B47",
                        fg="white",
                        justify="left",
                    ).pack(fill="both", padx=30, pady=10)

                elif f == 3:
                    tk.Label(
                        rwframe,
                        text=f"La resistencia equivalente es: {r_e}",
                        bg="#2A3B47",
                        fg="white",
                        justify="left",
                    ).pack(fill="both", padx=30, pady=10)

            elif k == 2:
                tk.Label(
                    rwframe,
                    text=f"Uno o mas campos se encuentran\nincompletos o con un valor erroneo.\n"
                         f"Los campos solo admiten numeros\ndecimales positivos.",
                    bg="#2A3B47",
                    fg="white",
                ).pack(fill="both", padx=30, pady=10)

            else:
                print("wtf how did we get here")

        rwframe.grid(row=0, column=2, sticky="nesw")


def clear_widgets(ptl):
    for widget in ptl.winfo_children():
        widget.destroy()


def load_main_frame(frm):

    clear_widgets(frm)

    mainframe.tkraise()

    rwframe.grid_forget()

    mainframe.pack_propagate(False)

    tk.Label(
        mainframe,
        text="RESISTANCE CALCULATOR",
        bg=bgclr,
        fg="white",

    ).pack(pady=30)

    tk.Button(
        mainframe,
        text="Serie",
        width=20,
        cursor="hand2",
        command=lambda: load_frame1(mainframe),

    ).pack(pady=10)

    tk.Button(
        mainframe,
        text="Paralelo",
        width=20,
        cursor="hand2",
        command=lambda: load_frame2(mainframe),

    ).pack(pady=10)

    tk.Button(
        mainframe,
        text="Paralelo 2 Resistencias",
        width=20,
        cursor="hand2",
        command=lambda: load_frame3(mainframe),

    ).pack(pady=10)

    tk.Button(
        mainframe,
        text="Salir",
        width=20,
        cursor="hand2",
        command=lambda: exit(),

    ).pack(pady=50)


def load_frame1(frm):

    clear_widgets(frm)

    frame1.tkraise()

    frame1.pack_propagate(False)

    voltaje = tk.Entry(frame1)
    r1 = tk.Entry(frame1)
    r2 = tk.Entry(frame1)
    r3 = tk.Entry(frame1)
    img = Image.open(rspng)
    img = img.resize((100, 75), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    photolabel = tk.Label(frame1, image=image)
    photolabel.image = image

    tk.Label(
        frame1,
        text="Serie",
        bg=bgclr,
        fg="white",

    ).pack(pady=10)

    photolabel.pack()

    tk.Label(
        frame1,
        text="Voltaje:",
        bg=bgclr,
        fg="white",

    ).pack()

    voltaje.pack(pady=5)

    tk.Label(
        frame1,
        text="R1",
        bg=bgclr,
        fg="white",

    ).pack()
    r1.pack()

    tk.Label(
        frame1,
        text="R2",
        bg=bgclr,
        fg="white",

    ).pack()
    r2.pack()

    tk.Label(
        frame1,
        text="R3",
        bg=bgclr,
        fg="white",

    ).pack()
    r3.pack()

    tk.Button(
        frame1,
        text="Resultado",
        width=10,
        height=2,
        cursor="hand2",
        command=lambda: result_button(1, voltaje.get(), r1.get(), r2.get(), r3.get()),

    ).pack(pady=10, after=r3)

    tk.Button(
        frame1,
        text="Atrás",
        width=20,
        cursor="hand2",
        command=lambda: load_main_frame(frame1),

    ).pack(pady=10, after=r3, side=tk.BOTTOM)


def load_frame2(frm):

    clear_widgets(frm)

    frame2.tkraise()

    frame2.pack_propagate(False)

    voltaje = tk.Entry(frame2)
    r1 = tk.Entry(frame2)
    r2 = tk.Entry(frame2)
    r3 = tk.Entry(frame2)
    img = Image.open(rppng)
    img = img.resize((100, 75), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    photolabel = tk.Label(frame2, image=image)
    photolabel.image = image

    tk.Label(
        frame2,
        text="Paralelo",
        bg=bgclr,
        fg="white",

    ).pack(pady=10)

    photolabel.pack()

    tk.Label(
        frame2,
        text="Voltaje:",
        bg=bgclr,
        fg="white",

    ).pack()

    voltaje.pack(pady=5)

    tk.Label(
        frame2,
        text="R1",
        bg=bgclr,
        fg="white",

    ).pack()
    r1.pack()

    tk.Label(
        frame2,
        text="R2",
        bg=bgclr,
        fg="white",

    ).pack()
    r2.pack()

    tk.Label(
        frame2,
        text="R3",
        bg=bgclr,
        fg="white",

    ).pack()
    r3.pack()

    tk.Button(
        frame2,
        text="Resultado",
        width=10,
        height=2,
        cursor="hand2",
        command=lambda: result_button(2, voltaje.get(), r1.get(), r2.get(), r3.get()),

    ).pack(pady=10, after=r3)

    tk.Button(
        frame2,
        text="Atrás",
        width=20,
        cursor="hand2",
        command=lambda: load_main_frame(frame2),

    ).pack(pady=10, after=r3, side=tk.BOTTOM)


def load_frame3(frm):

    clear_widgets(frm)

    frame3.tkraise()

    frame3.pack_propagate(False)

    r1 = tk.Entry(frame3)
    r2 = tk.Entry(frame3)
    img = Image.open(rpjpng)
    img = img.resize((100, 75), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    photolabel = tk.Label(frame3, image=image)
    photolabel.image = image

    tk.Label(
        frame3,
        text="Paralelo 2 Resistencias",
        bg=bgclr,
        fg="white",

    ).pack(pady=10)

    photolabel.pack()

    tk.Label(
        frame3,
        text="R1",
        bg=bgclr,
        fg="white",

    ).pack()
    r1.pack()

    tk.Label(
        frame3,
        text="R2",
        bg=bgclr,
        fg="white",

    ).pack()
    r2.pack()

    tk.Button(
        frame3,
        text="Resultado",
        width=10,
        height=2,
        cursor="hand2",
        command=lambda: result_button(3, 0, r1.get(), r2.get(), 0),

    ).pack(pady=40)

    tk.Button(
        frame3,
        text="Atrás",
        width=20,
        cursor="hand2",
        command=lambda: load_main_frame(frame3),

    ).pack(pady=10, side=tk.BOTTOM)


mw = tk.Tk()
mw.title("Resistance Calculator")
mw.resizable(False, False)
mw.iconbitmap(icon)
mainframe = tk.Frame(mw, width=350, height=400, bg=bgclr)
frame1 = tk.Frame(mw, width=350, height=400, bg=bgclr)
frame2 = tk.Frame(mw, width=350, height=400, bg=bgclr)
frame3 = tk.Frame(mw, width=350, height=400, bg=bgclr)
rwframe = tk.Frame(mw, width=200, height=200, bg=bgclr)

for frame in (mainframe, frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nesw")


load_main_frame(mainframe)
mw.mainloop()

from tkinter import (
    Tk,
    messagebox,
    Label,
    Text,
    Entry,
    OptionMenu,
    Button,
    StringVar,
    GROOVE,
    END,
)
from keras_nlp.models import GPT2CausalLM
from keras_nlp.models import OPTCausalLM


def basla():
    if ent1.get() == "clear" or ent1.get() == "Clear" or ent1.get() == "CLEAR":
        answer.delete("1.0", END)
        ent1.delete(0, "end")

    else:
        if label_option.get() == "GPT2CausalLM":
            gpt2_lm = GPT2CausalLM.from_preset("gpt2_base_en")
            prompt = ent1.get()
            answer.delete("1.0", END)
            result = gpt2_lm.generate(prompt, max_length=1024)
            answer.insert(END, result)

        elif label_option.get() == "OPTCausalLM":
            opt_lm = OPTCausalLM.from_preset("opt_125m_en")
            prompt = ent1.get()
            answer.delete("1.0", END)
            result = opt_lm.generate(prompt, max_length=1024)
            answer.insert(END, result)

        else:
            messagebox.showwarning("Uyarı", "Model secilmemistir.")


main = Tk()
main.title("KerasNLP")
main.geometry(f"{main.winfo_screenwidth() - 50}x{main.winfo_screenheight() - 50}")
main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: basla())


Label(main, text="Lütfen Prompt giriniz: ").place(x=40, y=20)

ent1 = Entry(main, width=120)
ent1.place(x=200, y=20)

label_option = StringVar(main)
label_open_menu = OptionMenu(main, label_option, "GPT2CausalLM", "OPTCausalLM").place(
    x=main.winfo_screenwidth() - 190, y=20
)


Button(
    main,
    text="Cevapla",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=basla,
).place(x=main.winfo_screenwidth() - 150, y=20)


Label(main, text="Cevap: ").place(x=50, y=60)
answer = Text(main, width=150, height=35)
answer.place(x=50, y=80)

main.mainloop()

# -*- coding: utf-8 -*-
"""Abstract text summarization using pegasus
# 0. Install dependencies
"""
import tkinter as tk
import torch
import transformers
import sentencepiece

# #from tkinter import messagebox
# # Install PyTorch
# # Install transformers
#
#
def summarize():
   # print("enter passage:\n")

    """# 1. Import and Load Model"""
    # Importing dependencies from transformers
    from transformers import PegasusForConditionalGeneration, PegasusTokenizer
    # Load tokenizer
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

    # Load model
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    """# 2. Perform Abstractive Summarization"""
    text =inptext.get('1.0',"end").strip()

    # Create tokens - number representation of our text
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    # Input tokens
    tokens
    # Summarize
    summary = model.generate(**tokens)
    # Output summary tokens
    summary[0]
    # Decode summary
    result=tokenizer.decode(summary[0])
    result
    '''command output'''
    print("summary is: \n",result)

    summaryf.config(state='normal')

    summaryf.insert('1.0',result)


    summaryf.config(state='disabled')




root = tk. Tk()
root.title("Text Summarizer")
root.geometry('1280x720')
root.configure(bg='#ffffff')





t1label= tk. Label (root, text="Enter The Passage")
t1label.pack()

inptext= tk.Text(root, height=13, width=140)
inptext.config(bg='#ddd6dd')
inptext.pack()

btn=tk.Button(root,text='SUMMARIZE',command=summarize)
btn.pack()

t2label= tk. Label (root, text="Summary of the Aritcle")
t2label.pack()


summaryf = tk.Text(root, height=13, width=140)
summaryf.config(state='disabled', bg='#dddddd')
summaryf.pack()


t3label= tk. Label (root, text="Abstractive text summarization "

                    )
t3label.pack()



root.mainloop()




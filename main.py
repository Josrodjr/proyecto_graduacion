import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# tkinter for the GUI
import tkinter as tk
from tkinter import Tk, scrolledtext, Label, W, S, E, N, Button, END, Frame, Entry
from tkinter.scrolledtext import ScrolledText

import random


class Prototype(Frame):
    # for the regression
    vectorizer = CountVectorizer()
    classifier = LogisticRegression()

    instruction_label = Label()
    text_frame = ScrolledText()
    process_btn = Button()
    generate_eval = Button()
    doc_entry = Entry()
    predicted_label = Label()
    predicted_result = Label()
    result_description = Label()


    def __init__(self, master=None):

        super(Prototype, self).__init__()

        self.master = master
        self.master.title('App')
        self.master.geometry('570x200')
        

        # labels
        self.instruction_label = Label(self.master, text="Inserte un texto para analizar: ")
        self.instruction_label.grid(row=0, sticky=W)

        # input
        self.text_frame = ScrolledText(self.master, width=45,height=3)
        self.text_frame.grid(column=1,row=0)

        # button
        self.process_btn =  Button(self.master, text ="Test Microblog", command = self.test_expression)
        self.process_btn.grid(row=1, column =1)

        # charge the predictive model using the data provided
        self.generate_eval = Button(self.master, text ="Load Predictive model", command = self.load_model)
        self.generate_eval.grid(row=2, column =0)


        # add an entry with the value of the document thats used for changig the data
        self.doc_entry = Entry(self.master)
        self.doc_entry.grid(row=1, column=0)
        self.doc_entry.insert(END, 'prototipo_tweets.csv')

        # add a label for the prediction
        self.predicted_label = Label(self.master, text="Prediccion: ")
        self.predicted_label.grid(row=3, column = 1)

        # add a label for the prediction text
        self.predicted_result = Label(self.master, text="0")
        self.predicted_result.grid(row=3, column = 2)

        # add a label for the result drescription
        self.result_description = Label(self.master, text="For purposes of this program 1 is :( and 0 is :)")
        self.result_description.grid(row=4, column = 1)

    def test_expression(self):
        self.introduced_text = self.text_frame.get('1.0', END)
        # print(self.introduced_text)

        test_string = [self.introduced_text]
        # # vectorize
        test_string = self.vectorizer.transform(test_string)

        score2 = self.classifier.predict(test_string)

        # print("Test Acc: ", score2)
        self.predicted_result.configure(text = score2)
        # self.predicted_result.configure(text = random.randint(0,1))

    def load_model(self):
        df = pd.read_csv('prototipo_tweets.csv')

        text = df['text'].values
        y = df['sentiment'].values

        sentences_train, sentences_test, y_train, y_test = train_test_split(text, y, test_size=0.25, random_state=1000)

        
        self.vectorizer.fit(sentences_train)

        X_train = self.vectorizer.transform(sentences_train)
        X_test  = self.vectorizer.transform(sentences_test)
        # print(X_train)

        self.classifier.fit(X_train, y_train)
        score = self.classifier.score(X_test, y_test)

        print("Current Accuracy: ", score)



root = tk.Tk()

proto = Prototype(root)

proto.mainloop()


# df = pd.read_csv('prototipo_tweets.csv')

# # print(df.iloc[0])

# text = df['text'].values
# y = df['sentiment'].values

# sentences_train, sentences_test, y_train, y_test = train_test_split(text, y, test_size=0.25, random_state=1000)

# vectorizer = CountVectorizer()
# vectorizer.fit(sentences_train)

# X_train = vectorizer.transform(sentences_train)
# X_test  = vectorizer.transform(sentences_test)
# # print(X_train)

# classifier = LogisticRegression()
# classifier.fit(X_train, y_train)
# score = classifier.score(X_test, y_test)

# # print(sentences_test)

# # test_string = ["deprimido agobiado ansioso ansiedad triste sufriendo cuarentena ayuda"]
# test_string = ["si"]
# # vectorize
# test_string = vectorizer.transform(test_string)

# score2 = classifier.predict(test_string)

# print("Test Acc: ", score2)

# print("Accuracy:", score)


# window.title("App")

# window.geometry('570x200')

# # labels
# Label(window, text="Inserte un texto para analizar: ").grid(row=0, sticky=W)

# # text input
# txt = scrolledtext.ScrolledText(window,width=45,height=3)
# txt.grid(column=1,row=0)

# Button(window, text ="Test Microblog", command = test_string).grid(row=1)

# Introduction to Python

## Credits
Portions of the material for this introduction to Python is derived from the book [Python Crash Course - Third Edition](https://nostarch.com/python-crash-course-3rd-edition).  It's available where ever you purchase your books.

### Introduction

Python is a general-purpose, high-level programming language. It is interpreted, meaning that it does not need to be compiled into machine code before it can be run. Python is known for its simple syntax and readability, making it a popular choice for beginners and experienced programmers alike.

Python was created in the late 1980s by Guido van Rossum, a Dutch computer scientist. Van Rossum was looking for a language that was more readable and easier to use than the languages that were available at the time. He named the language Python after the British comedy troupe Monty Python, because he was a fan of their work and wanted a name that was "short, unique, and slightly mysterious".

Python was first released in 1991, and it quickly gained popularity among programmers. It was used to develop a wide variety of applications, including web applications, desktop applications, and scientific computing applications.  Python is a cross-platform programming language, which means it runs on all the major operating systems. Any Python program you write should run on any modern computer that has Python installed. 

Python is a versatile language that can be used for a wide variety of tasks. It is commonly used for:

* **Web development**: Python can be used to develop both the front-end and back-end of web applications. It is a popular choice for developing web frameworks such as Django and Flask.
* **Software development**: Python can be used to develop desktop applications, mobile applications, and server-side applications. It is also used for developing machine learning and artificial intelligence applications.
* **Data science and machine learning**: Python is a popular choice for data science and machine learning tasks. It has a number of libraries and frameworks that are specifically designed for these tasks, such as NumPy, Pandas, and scikit-learn.
* **Automation**: Python can be used to automate a variety of tasks, such as system administration, data processing, and web scraping.

Python is a popular language for beginners because it is relatively easy to learn. The syntax is simple and readable, and there are a number of resources available to help beginners learn the language. Python is also a popular language for experienced programmers because it is versatile and powerful.

Here are some of the advantages of using Python:

* **Simple syntax**: Python has a simple and readable syntax, making it easy to learn and use.
* **Versatility**: Python can be used for a wide variety of tasks, from web development to data science to automation.
* **Power**: Python is a powerful language that can be used to develop complex applications.
* **Large community**: Python has a large and active community of users and developers. This means that there are a number of resources available to help you learn and use the language.

If you are interested in learning a programming language, Python is a great choice. It is relatively easy to learn, versatile, and powerful.

## Getting Started

### Installing Python

Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers now come with Python already installed. If you do need to install Python and aren't confident about the task you can find a few notes on the [BeginnersGuide/Download wiki page](https://wiki.python.org/moin/BeginnersGuide/Download), but installation is unremarkable on most platforms.

#### Coding Tools

Every Python installation comes with an **Integrated Development and Learning Environment**, which you’ll see shortened to IDLE or even IDE. These are a class of applications that help you write code more efficiently. While there are many IDEs for you to choose from, Python IDLE is very basic, which makes it the perfect tool for a beginning programmer.

Python IDLE comes included in Python installations on Windows and Mac. If you’re a Linux user, then you should be able to find and download Python IDLE using your package manager. Once you’ve installed it, you can then use Python IDLE as an interactive interpreter or as a file editor:

![](images/python-idle.png)

For our lab, we'll be using **Visual Studio Code**, a free coding editor that helps you start coding quickly. Use it to code in any programming language, without switching editors. Visual Studio Code has support for many languages, including Python, Java, C++, JavaScript, and more.

Visual Studio Code is built with extensibility in mind. From the UI to the editing experience, almost every part of VS Code can be customized and enhanced through the Extension API. In fact, many core features of VS Code are built as extensions and use the same Extension API.

![](images/vscode.png)

We'll be using a Python extension to help guide us through the coding exercises:

![](images/python-extension.png)

Of course, you can choose to use the command line interface (CLI) to write and execute Python scripts. It's straightforward and simple but can become a bit cumbersome when you begin to write more advanced applications.

```
C:\> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ^Z

C:\>
```

```
C:\> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```

Create a file called `hello_world.py` and enter the following line in the editor:

```
print("Hello Python world!")
```

Enter the following commands to run `hello_world.py`:

```
C:\> python hello_world.py
Hello Python world!
```

## Resources

[Python Documentation](https://docs.python.org/3/)


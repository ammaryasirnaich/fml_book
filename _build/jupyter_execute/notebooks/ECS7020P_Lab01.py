#!/usr/bin/env python
# coding: utf-8

# # Lab 1: Introduction
# 
# **Machine learning** provides computational tools to extract knowledge from data. Therefore, to build and deploy machine learning solutions we need to use a  **data science computing environment**.
# 
# **Python**-based computing environments are one of the most popular options among data scientists. Python provides standard, **in-built** functionalities that can be extended **importing** third-party packages. Some of the most common third-party libraries include NumPy, Pandas, Matplotlib and Scikit-learn.
# 
# 
# ECS7020P labs use **Python-powered Jupyter notebooks** to create **interactive** data science computing environments. A Jupyter notebook consists of **code cells** that contain code that can be executed, and **text cells** that are used for documetation purposes. Jupyter notebooks are powered by an **engine**, in our case Python, that can be on your machine (**local runtime**) or hosted on a remote, cloud-based machine (**hosted runtime**). The instructions in each lab will assume that you are using **Google Colab**, but you should be able to use other runtimes too. If you choose other runtimes you might need to do some minor tweaks, such as installing a library that is provided by the Google Colab environment by default.
# 
# The purpose of this lab is to familiarise ourselves with our Python environment. Once you've completed this lab, you will be able to attempt a quiz on QM+ that is worth **2 marks**.

# # Running a code cell
# 
# Click on this text, and cell that contains it will be highlighted. Double-click on it, and you will be able to edit it. 
# 
# Text cells (also known as markdown cells) allow you to document your work. You can use different fonts, add titles, include resources such as images and even write nice mathematical expression, for instance
# 
# $\begin{equation}
# f(x) = w_0 + w_1 x
# \end{equation}$
# 
# To write such nice mathematical expressions, you need to use a different markup language called Latex.
# 
# Code cells, such as the one below this text cell, contain code that can be executed. In the example below, we first create the variable `mystring` by assigning the string value `"Welcome to ECS7020P!"` and then we print it. You can run it by clicking on the play button on the left. Any output will appear underneath.

# In[1]:


mystring = "Welcome to ECS7020P!"
print(mystring)


# Note that if you are using Google Colab, it might take a while to run your first cell. The reason is that Google needs to allocate some computing resources first, so nothing to worry about.
# 
# Here is another example, where we create an integer variable `myint`: 

# In[2]:


myint = 42


# You will have noticed that running the cell didn't produce any output. The variable has however been created, as you can see if you use the command `whos`:

# In[3]:


whos


# Using `print`, you can check the value of `myint`:   

# In[4]:


print("The ultimate answer to life, the universe and everything is...", myint)


# Very easy.

# # Uploading files
# 
# Machine learning extracts knowledge from data. Therefore, we need to make our data available to the machine that is running our code. If you are running your Jupyter notebook on Google Colab, then we'll need to make sure Colab's runtime has access to our data.
# 
# There are different ways to make our data accessible, but here we will present the easiest one:
# 
# - Find the `Files` icon on the left pane and click on it.
# - Click on the `Upload` icon.
# - Select the file that you want to upload from your local machine.
# 
# Note that you will not be able to upload a file if your notebook has not been allocated any Colab computing resources. Also note that your notebook will be disconnected if left idle for too long and after 12 hours. Disconnection will result in your data being lost.
# 
# Now it's your turn. Have a go at uploading the CSV file `AnimalsHRvsBM.csv`. Once uploaded, you should be able to see it on the left-hand pane.
# 
# 

# # Importing libraries
# 
# You can add new functionality to your Python Jupyter notebook environment by importing libraries. Let's import Pandas, one of the most popular Python libraries for working with structured data.

# In[5]:


import pandas as pd


# We can use Pandas to load the CSV file that we have just uploaded.

# In[6]:


df = pd.read_csv('../datasets/AnimalsHRvsBM.csv')


# The variable `df` is a Pandas DataFrame, a table-like data structure consisting of rows and columns. The easiest way to print a Pandas DataFrame is as follows:

# In[7]:


df


# The DataFrame `df` records the average body mass (`BM`) and heart rate (`HR`) of 28 different animal species, from the little wild mouse to the massive humpback whale. Let's plot this dataset.
# 

# In[8]:


df.plot.scatter(x="BM (g)", y="HR (bpm)", logx=True)


# This concludes this short introductory lab. Feel free to experiment with this notebook, add new cells or edit existing ones, it's all yours! If you want to use the original Jupyter notebook, you can always download it from QM+.
# 
# 
# When you've finished playing, complete a short quiz on QM+ and earn 2 marks!
# 

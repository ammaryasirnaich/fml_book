Hello to Fundamentals of Machine learning!  You have just landed to the page where
you can learn how to generate book contents like this one using the **Jupyterbook**
You can install jupyterbook with pip or conda:

> pip install -U jupyter-book \
> or \
> conda install -c conda-forge jupyter-book

# Quickly generate a sample book
You can creat a sample book which works as a template to re-structure the contents including the look and feel of the book.
To generate this template book structure you just have to run the below command.
```
jupyter-book create mynewbook
```

# Structure of a Jupyter Book
After running the  `jupyter-book create` command `_config.yml` and `_toc.yml` files will be created.
The `_config.yml` contains the allowed configuration setting for the look and feel settings of the book while the `_toc.yml` contain the table of content settings for the book.





### Or using the already created Structure
For the fml book we have already created a structure which is as below:

> fml_book_content \ \
>  ..\ dataset \
>  ..\ images \
>  ..\ notebooks \
>  ..

```
Note: you can use ' git clone https://github.com/ammaryasirnaich/fml_book.git ' to clone this structure localy.
```
In this structure you can put your datasets,images and jupyter notebooks inside the corresponding folders so that while generating the book these resources can be included when the book in compiled. 
After you can also re-configured the `_config.yml and _toc.yml` files you can build the book running the `juyter-book build` command.
In our case we will run the command to build all the content of the jupyter book using the `-all` parameter.
```
jupyter-book build --all fml_book_content/
```

After running the above command the `_build` folder will be created containing `html` and `jupyter_execute` folders. Inside the `html` folder, their lies 
the web-based book for the fml which can be launched by double-clicking the `index.html` file.

>Note: \
In our case we would only modify the `_toc.yml` file in which we will included the chapters of the books by including the references-path of the  jupyter notebook or markdown files.
The order of the reference-path will suggest the chapter number automatically.



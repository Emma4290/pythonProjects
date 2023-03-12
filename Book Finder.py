book_year = float(input("What year was the book written? "))
nineteenth_century = float(book_year) <= 1899
twentieth_century = float(book_year) >= 1900

noughties = float(book_year) <= 1809
tens = float(book_year) <= 1819
twenties = float(book_year) <= 1829
thirties = float(book_year) <= 1839
forties = float(book_year) <= 1849
fifties = float(book_year) <= 1859
sixties = float(book_year) <= 1869
seventies = float(book_year) <= 1879
eighties = float(book_year) <= 1889
nineties = float(book_year) <= 1899

noughties1 = float(book_year) <= 1909
tens1 = float(book_year) <= 1919
twenties1 = float(book_year) <= 1929
thirties1 = float(book_year) <= 1939
forties1 = float(book_year) <= 1949
fifties1 = float(book_year) <= 1950


if nineteenth_century and noughties:
    print("Nineteenth century, noughties")

elif nineteenth_century and tens:
    print("Nineteenth century, tens")

elif nineteenth_century and twenties:
    print("Nineteenth century, twenties")

elif nineteenth_century and thirties:
    print("Nineteenth century, thirties")

elif nineteenth_century and forties:
    print("Nineteenth century, forties")

elif nineteenth_century and fifties:
    print("Nineteenth century, fifties")

elif nineteenth_century and sixties:
    print("Nineteenth century, sixties")

elif nineteenth_century and seventies:
    print("Nineteenth century, seventies")

elif nineteenth_century and eighties:
    print("Nineteenth century, eighties")

elif nineteenth_century and nineties:
    print("Nineteenth century, nineties")

elif twentieth_century and noughties1:
    print("Twentieth century, noughties")

elif twentieth_century and tens1:
    print("Twentieth century, tens")

elif twentieth_century and twenties1:
    print("Twentieth century, twenties")

elif twentieth_century and thirties1:
    print("Twentieth century, thirties")

elif twentieth_century and forties1:
    print("Twentieth century, forties")

elif twentieth_century and fifties1:
    print("Twentieth century, fifties")

else:
    print("Twentieth century post 1951")
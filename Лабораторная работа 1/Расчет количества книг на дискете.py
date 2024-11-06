# TODO Найдите количество книг, которое можно разместить на дискете

disk_mb = 1.44

pages = 100
lines = 50
symbols = 25
byte = 4

book_size_byte = pages * lines * symbols * byte
disk_byte = disk_mb * 1024 ** 2

count_books = int(disk_byte // book_size_byte)




print("Количество книг, помещающихся на дискету:", count_books)

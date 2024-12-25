from contextlib import contextmanager



@contextmanager
def file_manejer(file_name,mode):

    f=None
    try:
        if "." not in file_name :
            raise NameError
        print(f"file {file_name}  ochilyapdi")
        f=open(file_name,mode)
        yield f
    finally:
        if f:
            print(f"file  {file_name}  yopilyapdi")
            f.close()
with file_manejer('class_cantext.py','r') as file:
    a=file.read()
    print(a)
import inspect
import sys
import cStringIO
import os.path

if __name__ == '__main__':
    module_name = sys.argv[1].strip(".py")
    module = __import__(module_name)
    code_buffer = cStringIO.StringIO()
    for class_decl in inspect.getmembers(module, inspect.isclass):
        class_name = class_decl[0]
        l = "%s: class {\n" % (class_name)
        code_buffer.write(l)
        code_buffer.write("}\n\n")
        print inspect.getsourcelines(class_decl[1])
    ooc_name = "%s.ooc" % module_name


    #if not os.path.isfile(ooc_name):
    with open(ooc_name, "wb") as f:
        f.write(code_buffer.getvalue())
        print code_buffer.getvalue()



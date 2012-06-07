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
        code_buffer.write(l) # class name, e.g. "A: class {"

        """
        # getsourcelines gives back a tuple like
        # (['class A:\n', '    pass\n'], 1)
        """

        code_buffer.write("/*\n") # commenting out the python code
        body = inspect.getsourcelines(class_decl[1])[0]
        for line in body[1:]: # no need to keep the class header
            code_buffer.write(line)
        code_buffer.write("*/\n") # uncommenting
        code_buffer.write("}\n\n")

    ooc_name = "%s.ooc" % module_name


    #if not os.path.isfile(ooc_name):
    with open(ooc_name, "wb") as f:
        f.write(code_buffer.getvalue())
        print code_buffer.getvalue()



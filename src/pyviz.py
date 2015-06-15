import gdb

global path
path = [];

def is_container(v):
    c = v.type.code
    return (c == gdb.TYPE_CODE_STRUCT or c == gdb.TYPE_CODE_UNION)

def is_pointer(v):
    return (v.type.code == gdb.TYPE_CODE_PTR)

def print_struct_follow_pointers(s, file, level = 0, counter = 0):
    indent = ' '
    
    if not is_container(s):
        if counter != 0:
            file.write('%s | ' % (s,))
        return
    if counter != 0:
        file.write('%s%s%s [ shape=record, label=\"' % (indent,s.type, counter))
    for k in s.type.keys():
        v = s[k]
        if is_pointer(v):
            if counter != 0:
                file.write('%s%s | ' % (indent, k))
            try:
                v1 = v.dereference()
                v1.fetch_lazy()
            except gdb.error:
                continue
            path.append(v1)
        elif is_container(v):
            if counter != 0:
                file.write('%s | ' % (indent, k))
            path.append(v)
        else:
            if counter != 0:
                file.write('%s<%s>%s | ' % (indent, k, v))
    if counter != 0:
        file.write('%s\"];\n' % (indent,))
    
    if len(path) > 0:
        temp_nm = path.pop()
        print_struct_follow_pointers(temp_nm, file, level + 1, counter + 1)
        
        
        
class PrintStructFollowPointers(gdb.Command):
    '''
    visualize STRUCT-VALUE
    '''
    def __init__(self): 
        super(PrintStructFollowPointers, self).__init__(
            'visualize',
            gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)

    def invoke(self, arg, from_tty):
        try:
            v = gdb.parse_and_eval(arg)
        except gdb.error, e:
            raise gdb.GdbError(e.message)
        
        f = open('raw.txt', 'w+')
        f.write("digraph {\n")
        f.write("graph[rankdir=\"LR\"];\n")
        f.write("node[shape=record];\n")

        print_struct_follow_pointers(v, f)
        f.write('}')
        f.close()
        gdb.write("Saved as raw file\n")
        

PrintStructFollowPointers()
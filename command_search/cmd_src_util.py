import optparse
import sqlite3
import re

parser = optparse.OptionParser()

parser.add_option('-t', '--table', action = 'store', type='string', dest='table')
parser.add_option('-f', '--format', action = 'store_true', dest = 'format')
parser.add_option('-n', '--nooutput', action = 'store_false',dest = 'noop')
parser.add_option('-o', '--output', action = 'store', type='string', dest='outfile')

options, args = parser.parse_args()

def regexp(expr,item):
    reg = re.compile(expr)
    return reg.search(item) is not None

mydb = sqlite3.connect("../db_gen/cs_terms.db")
mydb.create_function("REGEXP", 2, regexp)
cur = mydb.cursor()

'''
#just checking table type
ur.execute("pragma table_info [%s]" %(options.table))
results = cur.fetchall()
for record in results:
    print record
'''

cur.execute('select * from %s where term REGEXP "%s"' %(options.table,args[0]))
results = cur.fetchall()

if options.outfile:
    fout = open(str(options.outfile),"w")
    for record in results:
        fout.write(record[1]+'\n')
    fout.close()

if options.noop:
    for record in results:
        print record[1]



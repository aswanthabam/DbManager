from . import sqlite
import sys,getopt


def main(argv):
    for opt in argv:
        if opt == '-sqlite' or opt == '--sqlite':
            ind = argv.index(opt)+1
            try:
                dbname = argv[ind]
                sqlite(dbname).shell()
            except:
                print("Er::Excepted File name as the second argument type 'python DataBaseManager -h' for help")
            
        elif opt == '-help' or opt == '--help' or opt == '-h':
            print('python DataBaseManager [option] <inputfile>\n\n[option]\n -sqlite  for using sqlite')
            sys.exit(2)
#dbname = sys.argv[1]
#sqlite(dbname).shell()
if __name__ == '__main__':
    main(sys.argv[1:])

import pickle
import nester


man = []
other = []
try:
    with open('.//chapter3//sketch.txt') as data:
        # out = open('.//chapter3//data.out', 'a')
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
    # print(man, file=out)
    # print(other, file=out)
    # out.close()
except IOError as err:
    print('The datafile is missing!' + '\n\t' + str(err))
try:
    with open('.//chapter3//man_data.dat', 'wb')as man_out,\
            open('.//chapter3//other_data.dat', 'wb')as other_out:
        pickle.dump(man, man_out)
        pickle.dump(other, other_out)
except IOError as err:
    print('File Error\n\t'+str(err))
except pickle.PickleError as perr:
    print('Pickle Error\n\t'+str(perr))

try:
    with open('.//chapter3//man_data.dat', 'rb') as man_in,\
            open('.//chapter3//other_data.dat', 'rb') as other_in:
        man_list = pickle.load(man_in)
        other_list = pickle.load(other_in)
    nester.print_lol(man_list, True, 1)
    nester.print_lol(other_list)
except IOError as err:
    print('File Error\n\t'+str(err))
except pickle.PickleError as perr:
    print('Pickle Error\n\t' + str(perr))
# try:
#     with open('.//chapter3//man_data.txt', 'w')as man_out,\
#             open('.//chapter3//other_data.txt', 'w')as other_out:
#         # print(man, file=man_out)
#         # print(other, file=other_out)
#         nester.print_lol(man, True, 1, man_out)
#         nester.print_lol(other, True, 2, other_out)
# except IOError as err:
#     print('File Erro \n\t' + str(err))
# try:
#     man_out = open('.//chapter3//man.out', 'w')
#     other_out = open('.//chapter3//other.out', 'w')
#     print(man, file=man_out)
#     print(other, file=other_out)
# except IOError as err:
#     print('File error.' + '\n\t' + str(err))
# finally:
#     if 'man_out' in locals():
#         man_out.close()
#     if 'other_out' in locals():
#         other_out.close()

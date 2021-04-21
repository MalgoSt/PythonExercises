def parser(text):
    """
    Zadanie:
    Funkcja, która dostaje na wejściu napis i zwraca napis.
    Jeśli w napisie wejściowym pojawi się sekwencja np. ‘4[kot]’ to zostanie zamieniona na ‘kotkotkotkot’.
    Krotność powtórzeń może być większa od 9. Sekwencje powtórzeń mogą być zagnieżdżone.
    """

    result = text
    openings = []   # list of lists: first index after opening bracket | number of repetitions | end of previous text
    s_number = ''   # number of repetitions as a string
    i = 0

    while i < len(result):
        val = result[i]
        # opening bracket
        if val == '[':
            if s_number == '':
                i_number = 1
            else:
                i_number = int(s_number)
            openings.append([i + 1, i_number, i - len(s_number)])

        # closing bracket
        elif val == ']' and len(openings) > 0:
            prev_len = len(result)
            text_repeated = openings[-1][1] * result[openings[-1][0]:i]
            result = result[0:openings[-1][2]] + text_repeated + result[i+1:len(result)]
            i += len(result) - prev_len   # index update because of the change of 'result'
            del openings[-1]

        # number of repetitions (if it comes before the opening bracket)
        if val.isdecimal():
            s_number += val
        else:
            s_number = ''
        i += 1

    return result


# test
def main():
    a = 'To 2[jest ]ćwiczenie 3[2[hip ]hura ]!'
    print(a)
    print(parser(a))
    print()
    a = 'To 2[jest4[!]]to12[.]'
    print(a)
    print(parser(a))
    print()
    a = 'Ala ma 31 lat i 2[bardzo3[!] ]pięknego kota, który nazywa się 2[Mru] 20[!].'
    print(a)
    print(parser(a))
    print()
    a = '[Ala] lubi 2[piękne 3[obrazki ]]z bożej łaski 123'
    print(a)
    print(parser(a))
    print()
    a = '15 3[kotów 2[Mruczków ]]i 5[1] psów [Reksio].'
    print(a)
    print(parser(a))
    print()
    a = '11[_2[Ala]] lubi koty.'
    print(a)
    print(parser(a))
    
    
if __name__ == '__main__':
    main()

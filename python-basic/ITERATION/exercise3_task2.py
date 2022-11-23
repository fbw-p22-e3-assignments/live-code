for j in range(0, 3):
    # print(f'*****OUTER ITERATION j={j}*****')
    for i in range(10):
        if i == 8:
            break
        # print(f'*****INNER ITERATION i={i}*****')
        # print(f'j={j}, i={i}')
        print(i + 10 * j, end=' ')
    print('\n')
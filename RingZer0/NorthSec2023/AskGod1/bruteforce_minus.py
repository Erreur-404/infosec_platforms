import string

hex_string = 'b0ad878fdaacd3acaabb87dbd6b7879887a8a8e0d4dfa9d5a0afdeae9dbb9987cdd9b6b4878ad8b5da99a9b3cab99bd19087a4878ecc9cccc9cacbcacc9bcb97cba09da098cbc89ccc9ecd9a9e9bcdc999cc9ecdc98e7471a9acaed0d57471baccd3cccabb87cdd3c8ce87add9b6b4878ad8b5da99a9b3cab99bd17471acb5cb'

for i in range(0, 256):
    result = ''.join(chr(int(hex_string[index:index+2], 16) - i) for index in range(0, len(hex_string), 2))
    if all(char in string.printable for char in result):
        print(f'i = {i}')

        if 'flag' in result or 'select' in result.lower() or 'SELECT' in result:
            print(f'Result: {result}')
            # with open(i, 'a') as f:
            #     print('Writing to file...')
            #     f.write('\n\n\n' + result)
            #     print('Done writing')
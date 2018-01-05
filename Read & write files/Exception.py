try:
    f = open('HowLongLyrics', 'r')
    content = f.read()

except Exception as e:
    print(e)

else: #replace this by finally to execute the next lines of codes regardless of the above lines
    words = content.split()
    for word in words:
        print('{0}: {1}'.format(word,words.count(word)))

'''some common errors:
except FileNotFoundError:
    print('Kiem tra lai ten file/File o trong may tinh')
except PermissionError:
    print('Kiem tra quyen truy cap cua file')
except ValueError:
    print('Kiem tra lai noi dung file')
'''



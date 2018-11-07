import difflib
import sys
import webbrowser

try:
    text_file_1 = sys.argv[1]
    print("text_file_1: " + text_file_1)
    text_file_2 = sys.argv[2]
    print("text_file_2: " + text_file_2)
except Exception as e:
    print("Error: " + str(e))
    print("1Usage: diff.py file_name1 file_name2")
    sys.exit()

def read_file(filename):
    try:
        file_handle = open(filename, 'r')
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as error:
        print("Read file Error: " + str(error))
        sys.exit()

if text_file_1 == "" or text_file_2 == "":
    print("2Usage: diff.py file_name1 file_name2")
    sys.exit()

text1_lines = read_file(text_file_1)
text2_lines = read_file(text_file_2)
d = difflib.HtmlDiff()
# print(d.make_file(text1_lines, text2_lines))

diff_result_html = open('diff_result.html', 'w', encoding='utf-8')
diff_result_html.write(d.make_file(text1_lines, text2_lines))
# webbrowser.open("www.baidu.com")

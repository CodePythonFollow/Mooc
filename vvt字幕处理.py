import os

def get_srt(dirname, file):
    fi = open(f'{dirname}/{file}', 'r', encoding='utf-8')
    fo = open(f"{file.replace('.vvt', '.srt')}", 'a', encoding='utf-8')

    lines = fi.readlines()

    for line in lines:
        if line == '\n':
            continue
        elif 'WEBVTT' in line:
            continue
        try:
            int(line[0])
            fo.write('\n\n' + line)
        except Exception as e:
            fo.write(line.strip('\n'))
    fi.close()
    fo.close()


if __name__ == '__main__':
    dirname = 'aa'
    datas = os.listdir(dirname)

    for file in datas:
        if '.vtt' in file:
            get_srt(dirname, file)

def solution(m, musicinfos):
    answer = []
    m = "".join(muf(m))
    for music in musicinfos:
        s,e,n,ms = music.split(',')
        a,b = s.split(":")
        s = int(a)*60 + int(b)
        a,b = e.split(":")
        e = int(a)*60 + int(b)
        time = e-s
        ms = muf(ms)
        nn = "".join((time//len(ms))*ms + ms[:(time%len(ms))])
        if m in nn:
            if answer:
                if int(answer[1]) < time:
                    answer = [n,time]
            else:
                answer = [n,time]
    if len(answer) == 0:
        return "(None)"
    return answer[0]

def muf(a):
    a = "".join(a)
    a = a.replace("C#","c")
    a = a.replace("D#","d")
    a = a.replace("F#","f")
    a = a.replace("G#","g")
    a = a.replace("A#","a")
    return list(a)
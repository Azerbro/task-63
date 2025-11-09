file = open('sport.txt', encoding = 'cp1251')
file.readline()

freq = {}
for st in file:
    cur = st.split('\t')
    sports = [sport.lower().strip() for sport in cur[3].split(',') if sport.strip()]
    for sport in sports:
        freq[sport] = freq.get(sport, 0) + 1

answer = sorted(freq.items(), key = lambda x: -x[1])

for sport, count in answer[:3]:
    print(sport, count)
    
file.close()

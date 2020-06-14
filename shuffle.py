import random , json
import pprint

with open('/home/welcome/Desktop/shuffle/studendName.json','r') as f:
    data=json.load(f)
with open('/home/welcome/Desktop/shuffle/room.json','r') as f:
    room=json.load(f)
name = data



bedN = [10,8,8]
def remove1(rem):
    for j in rem:
        name.remove(j)




def shuffle_bed(name,index):
    check = []
    My_list = [*range(1, bedN[index]+1, 1)]
    random.shuffle(My_list)
    for n in range(len(name)):
        check.append([name[n],My_list[n]])
    return(check)
   


index = 0
final = []
for i in room:
    dic = {}
    lr = random.sample(name, (room[i]))
    remove1(lr)
    s = shuffle_bed(lr,index)
    dic[i]=s
    final.append(dic)
    index = index + 1

for d in final:
    for room,value in d.items():
        # print(room)
        print ("Room Number ",room)
        for student in range(len(d[room])):
            print("  ",d[room][student][0] ,"--", d[room][student][1] )
    
json_object = json.dumps(final, indent = 4) 
  

with open("room_assginment.json", "w") as outfile: 
    outfile.write(json_object) 





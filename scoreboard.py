"""
Reply Code Challange 2019
Scoreboard Challange
Link of pdf (as on 19/3/2020 on Reply's website): https://challenges.reply.com/tamtamy/file/download-224904.action

"""

import numpy as np

def process(td,ut):
    
    
    scores = []
    penalties = []
    team_ids = []
    
    for k,v in td.items():
        scores.append(-(v[0]))
        penalties.append((v[1]))
        team_ids.append(k)
        
    inds = np.lexsort((team_ids,penalties,scores))
    res = []
    
    td = list(td.items())
    for i in inds:
        res.append(td[i][0])
        
    uts = sorted(list(ut))
    res.extend(uts)
    
    return res



def get_input(f):
    """ Pass the file handler"""
    n,l = [int(i) for i in f.readline().split(" ")]
   # logs = []
    teams_data = {} # team id: [score,penalty]
    unscored_teams = set([i for i in range(1,n+1)])
    team_probs_solved = {k:set() for k in range(1,n+1)}
    for i in range(l):
        ts,t,p,i,s = [int(i) for i in f.readline().split(" ")]
        if s == 1:
            if t in unscored_teams:
                unscored_teams.remove(t)
            if t in teams_data:
                    if str(p) + str(i) not in team_probs_solved[t]:
                        teams_data[t][0] += i
                        teams_data[t][1] += ts
            else:
                teams_data[t] = [i,ts]
            team_probs_solved[t].add(str(p)+str(i))
            
        #logs.append((ts,t,p,i,s))
    return (teams_data,unscored_teams)

def store_output(ans,t,f):
    """ Pass the vars to be written and file handler"""
    line = f"Case #{t}: " + " ".join([str(i) for i in ans]) 
    f.write(line + "\n")
    

for file in os.listdir("./Inputs"):
    if file[-4:] == ".txt":
        fi = open("./Inputs/" + file,"r")
        fo = open("./Outputs/output" + file[5:],"w")
        num_testcases = int(fi.readline())
        for test_case in range(num_testcases):
            inputs = get_input(fi)
            ans = process(*inputs)
            #print(ans)
            store_output(ans,test_case+1,fo)
        fo.close()
        fi.close()
        

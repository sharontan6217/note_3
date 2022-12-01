# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:21:17 2022

@author: Tan Xiao
"""

import pandas as pd
import numpy as np 
import os


data_alias = "C:/Users/smile/Documents/9102/assignment 3/data/"
log_alias = "C:/Users/smile/Documents/9102/assignment 3/log/"
output_alias = "C:/Users/smile/Documents/9102/assignment 3/output/"
input_alias = "C:/Users/smile/Documents/9102/assignment 3/"
data_all = "2017_ALL"
data_AST = "2017_AST"
data_BLK = "2017_BLK"
data_PTS = "2017_PTS"
data_STL = "2017_STL"
data_TRB = "2017_TRB"
data_extension = ".csv"
data_array = "input_type"
data_k = "input_k"
file_type = ".txt"


#--------Data Loading-----------#


def data_loading():
    df_all = pd.read_csv(data_alias+data_all+data_extension, skiprows=1,names=["ID","Player","Tm","TRB","AST","STL","BLK","PTS"],delimiter=",",na_filter=False)
    df_AST = pd.read_csv(data_alias+data_AST+data_extension, names=["ID","AST"], delimiter=",",na_filter=False).sort_values("AST",ascending=False)
    df_BLK = pd.read_csv(data_alias+data_BLK+data_extension, names=["ID","BLK"],delimiter=",",na_filter=False).sort_values("BLK",ascending=False)
    df_PTS = pd.read_csv(data_alias+data_PTS+data_extension, names=["ID","PTS"],delimiter=",",na_filter=False).sort_values("PTS",ascending=False)
    df_STL = pd.read_csv(data_alias+data_STL+data_extension, names=["ID","STL"],delimiter=",",na_filter=False).sort_values("STL",ascending=False)   
    df_TRB = pd.read_csv(data_alias+data_TRB+data_extension, names=["ID","TRB"],delimiter=",",na_filter=False).sort_values("TRB",ascending=False)

    return df_all, df_AST,df_BLK,df_PTS,df_STL,df_TRB,input_array

    
def benchmark(input_array,k):

    
    global df_all,df_AST,df_BLK,df_PTS,df_STL,df_TRB,ast,blk,pts,stl,trb,ast_max,blk_max,pts_max,stl_max,trb_max,types
    df_all, df_AST,df_BLK,df_PTS,df_STL,df_TRB,input_array = data_loading()

    

    weight=[]
    stats=[1,2,3,4,5]
    types=["TRB","AST","BLK","STL","PTS"]
    for ti in stats:
        if ti in input_array:
            input_type_ = types[ti-1]
            weight_ = 1
            weight.append([input_type_,weight_])
        elif ti not in input_array:
            input_type_ = types[ti-1]
            weight_ = 0
            weight.append([input_type_,weight_])
    df_weight = pd.DataFrame(data=weight,columns=("Input_Type","Weight"))
    print(weight,df_weight)       
    
        
        


    summary=[]
    input_weight=[]
    df_all["TRB"]=pd.to_numeric(df_all["TRB"],errors="coerce")
    df_all["AST"]=pd.to_numeric(df_all["AST"],errors="coerce")
    df_all["BLK"]=pd.to_numeric(df_all["BLK"],errors="coerce")
    df_all["STL"]=pd.to_numeric(df_all["STL"],errors="coerce")
    df_all["PTS"]=pd.to_numeric(df_all["PTS"],errors="coerce")
    ast_max=df_all["AST"].max()
    blk_max=df_all["BLK"].max()
    stl_max=df_all["STL"].max()
    trb_max=df_all["TRB"].max()
    pts_max=df_all["PTS"].max()

    types = df_all.columns[3:8]
   # print(df_all[df_all["ID"]==559])

    for i in range(len(df_weight)):
        for j in range(len(types)):
            if df_weight["Input_Type"][i]==types[j] and df_weight["Input_Type"][i]=="TRB":
                trb=df_weight["Weight"][i]
            elif df_weight["Input_Type"][i]==types[j] and df_weight["Input_Type"][i]=="AST":
                ast=df_weight["Weight"][i]
            elif df_weight["Input_Type"][i]==types[j] and df_weight["Input_Type"][i]=="BLK":
                blk=df_weight["Weight"][i]
            elif df_weight["Input_Type"][i]==types[j] and df_weight["Input_Type"][i]=="STL":
                stl=df_weight["Weight"][i]
            else:
                pts=df_weight["Weight"][i]
            j+=1
        i+=1


    df_all["TRB"]=(trb*df_all["TRB"])/trb_max
    df_all["AST"]=(ast*df_all["AST"])/ast_max
    df_all["BLK"]=(blk*df_all["BLK"])/blk_max
    df_all["STL"]=(stl*df_all["STL"])/stl_max
    df_all["PTS"]=(pts*df_all["PTS"])/pts_max 
    df_input=df_all
    for i in range (len(df_all)):
        summary_=df_all["TRB"][i]+df_all["AST"][i]+df_all["STL"][i]+df_all["BLK"][i]+df_all["PTS"][i]
        summary.append(summary_)
        i+=1
    df_all["Summary"]=summary
    df_benchmark=df_all.sort_values("Summary",ascending=False)
    print(df_benchmark)


    df_benchmark.to_csv(output_alias+str(input_array)+"Rankig of All Players by Benchmark"+data_extension)

    f=open (log_alias+"log.txt","a")
    f.write("---------------------------Assignment 3 ----------------------------------------- \n")
    f.write("Input Array is:{} \n".format(input_array))
    f.write("--------Assigment 3: Benchmark------------\n")
    f.write("The top k of the players of baseline algorithm is:{} \n".format(df_benchmark[0:k]))
    f.close()
    #print(df_benchmark[0:k])
    
    return df_all

def myNRA(input_array,k):

    df_TRB["TRB"]=pd.to_numeric(df_TRB["TRB"],errors="coerce")
    df_AST["AST"]=pd.to_numeric(df_AST["AST"],errors="coerce")
    df_BLK["BLK"]=pd.to_numeric(df_BLK["BLK"],errors="coerce")
    df_PTS["PTS"]=pd.to_numeric(df_PTS["PTS"],errors="coerce")
    df_STL["STL"]=pd.to_numeric(df_STL["STL"],errors="coerce")
    df_TRB["TRB"]=(trb*df_TRB["TRB"])/trb_max
    df_AST["AST"]=(ast*df_AST["AST"])/ast_max
    df_BLK["BLK"]=(blk*df_BLK["BLK"])/blk_max
    df_STL["STL"]=(stl*df_STL["STL"])/stl_max
    df_PTS["PTS"]=(pts*df_PTS["PTS"])/pts_max
    df_TRB["Type"]="TRB" 
    df_AST["Type"]="AST"
    df_BLK["Type"]="BLK"
    df_STL["Type"]="STL"
    df_PTS["Type"]="PTS"  

    print(df_BLK[df_BLK["ID"]==559]) 

    
    
    
    

    
    
    value_actual=[]
    id_total=[]
    type_total=[]
    value_total=[]
    data_query=[]
    
    data_max=[]
    count = 0
    for i in range(len(df_TRB)):
        data_output=[]
        data_id=[]
        value=[]
        data_type = []
        group_query=[]
        min_value=[]
        flag = 0
        data_id_ = [df_TRB["ID"][i],df_AST["ID"][i],df_BLK["ID"][i],df_STL["ID"][i],df_PTS["ID"][i]]
        value_ = [df_TRB["TRB"][i],df_AST["AST"][i],df_BLK["BLK"][i],df_STL["STL"][i],df_PTS["PTS"][i]]
        type_ = [df_TRB["Type"][i],df_AST["Type"][i],df_BLK["Type"][i],df_STL["Type"][i],df_PTS["Type"][i]]
        for i in range(len(data_id_)):
            data_id.append(data_id_[i])
            value.append(value_[i])
            data_type.append(type_[i])
            id_total.append(data_id_[i])
            value_total.append(value_[i])
            type_total.append(type_[i])
            i+=1
        
        
        df = pd.DataFrame({"ID":data_id,"Value":value,"Type":data_type})
        print(df)
        df_total = pd.DataFrame({"ID":id_total,"Value":value_total,"Type":type_total})
        for t in type_:
            min_ = df_total[df_total["Type"]==t]["Value"].min()
            min_value.append(min_)
            #print(max_value)
        
        for id_ in df["ID"]:
            value_trb = df[(df["ID"]==id_) & (df["Type"]=="TRB")]
            if len(value_trb)>0:
                value_trb = value_trb["Value"].values[0]
            else:
                value_trb = 0
            value_ast = df[(df["ID"]==id_) & (df["Type"]=="AST")]
            if len(value_ast)>0:
                value_ast = value_ast["Value"].values[0]
            else:
                value_ast = 0
            value_blk = df[(df["ID"]==id_) & (df["Type"]=="BLK")]
            if len(value_blk)>0:
                value_blk = value_blk["Value"].values[0]
            else:
                value_blk = 0            
            value_stl = df[(df["ID"]==id_) & (df["Type"]=="STL")]
            if len(value_stl)>0:
                value_stl = value_stl["Value"].values[0]
            else:
                value_stl = 0  
            value_pts = df[(df["ID"]==id_) & (df["Type"]=="PTS")]
            if len(value_pts)>0:
                value_pts = value_pts["Value"].values[0]
            else:
                value_pts = 0 



            data_query_ = [id_,value_trb,value_ast,value_blk,value_stl,value_pts]
            data_query.append(data_query_)
            #print("data_query is:",data_query)
            
            
        df_query_lb_=pd.DataFrame(data=data_query,columns=("ID","TRB","AST","BLK","STL","PTS")).drop_duplicates()
        print(df_query_lb_)
        df_query_lb=df_query_lb_.groupby("ID").sum().reset_index("ID")
        print(df_query_lb)
        for j in range(len(df_query_lb)):
            total_ = df_query_lb["TRB"][j]+df_query_lb["AST"][j]+df_query_lb["BLK"][j]+df_query_lb["STL"][j]+df_query_lb["PTS"][j]
            group_query_ = [df_query_lb["ID"][j],df_query_lb["TRB"][j],df_query_lb["AST"][j],df_query_lb["BLK"][j],df_query_lb["STL"][j],df_query_lb["PTS"][j],min_value[0],min_value[1],min_value[2],min_value[3],min_value[4],total_]
            group_query.append(group_query_)
        #print("group query is:",group_query_)
        
            
        df_query=pd.DataFrame(data=group_query,columns=("ID","TRB","AST","BLK","STL","PTS","UB_TRB","UB_AST","UB_BLK","UB_STL","UB_PTS","Total"))    
        df_query = df_query.sort_values("Total",ascending=False).reset_index()
        print(df_query)
        for n in range (len(df_query)):
            value_lb_ = df_query["TRB"][n]+df_query["AST"][n]+df_query["BLK"][n]+df_query["STL"][n]+df_query["PTS"][n]
            #print(n,"components values are:",df_query["AST"][n],df_query["BLK"][n],df_query["STL"][n],df_query["TRB"][n],df_query["PTS"][n],value_lb_)
            if df_query["AST"].values[n]>0:
                df_query["UB_AST"][n] = df_query["AST"].values[n]
            else: 
                pass
            if df_query["BLK"].values[n]>0:
                df_query["UB_BLK"][n] = df_query["BLK"].values[n]
            else:
                pass
            if df_query["STL"].values[n]>0:
                df_query["UB_STL"][n] = df_query["STL"].values[n]
            else:
                pass
            if df_query["TRB"].values[n]>0:
                df_query["UB_TRB"][n] = df_query["TRB"].values[n]
            else:
                pass
            if df_query["PTS"].values[n]>0:
                df_query["UB_PTS"][n] = df_query["PTS"].values[n]
            else:
                pass
            #print(i,df_query)
            value_ub_ = df_query["UB_TRB"].values[n]+df_query["UB_AST"].values[n]+df_query["UB_BLK"].values[n]+df_query["UB_STL"].values[n]+df_query["UB_PTS"].values[n]
            output=[df_query["ID"][n],value_lb_,value_ub_]
            data_output.append(output)
            df_output = pd.DataFrame(data=data_output,columns=("ID","Value_LB","Value_UB")).sort_values("Value_LB",ascending=False)
            
            if len(df_output)>=2*k:
                if df_output["Value_LB"][k-1]<max(df_output["Value_UB"][k:int(2*k-1)]):
                    continue
                else:
                    #print(df_output[0:2*k])
                    print("The count of lines is: ", count)

                    df_output.to_csv(output_alias+str(input_array)+"Ranking by Top K with NRA"+data_extension)


                    f=open (log_alias+"log.txt","a")
                    f.write("--------Assigment 3 Q1 : NRA------------\n")
                    f.write("The top k of the players based on NRA Algorithm is:{} \n".format(df_output[0:k]))
                    f.write("The count of lines is:{} \n".format(count))
                    f.close()   
                    exit()
            

            count+=1

            n+=1
        i+=1

    return df_output
        
def mySkyline(input_array,k):

    w=[]
    df_all_=df_all.copy(deep=True).sort_values("Summary",ascending=False)
    print(df_all_)

    df_all_["Flag"]=0


    for i in range(0,len(df_all)-1):
        df_all_.sort_values(["TRB","AST","BLK","STL","PTS"],ascending=False)
        df_all_.reset_index()
        

        if(df_all_["Flag"].values[i]==0):
            score=[]
            for ti in input_array:
                input_type_=types[ti-1]
                if df_all_[input_type_][i]>df_all_[input_type_][i+1]:
                    score.append(1)
                else:
                    score.append(0)
            print(i,sum(score))
            if len(w)==0:
                if sum(score)==len(input_array):
                    #print(df_all_.loc[i])
                    w.append(df_all_.loc[i])
                    df_all_["Flag"].values[i+1] = 1
                elif sum(score)==0:
                    #print(df_all_.loc[i+1])
                    w.append(df_all_.loc[i+1])
                    df_all_["Flag"].values[i] = 1
                else:
                    print(df_all_.loc[i])
                    w.append(df_all_.loc[i])
                    w.append(df_all_.loc[i+1])
                df_w = pd.DataFrame(data = w, columns=("ID","Player","Tm","TRB","AST","BLK","STL","PTS","Summary"))
                df_all_.reset_index()
                i+=1
            if len(w) > 0:
                if sum(score)==len(input_array):
                    #print(df_all_.loc[i])
                    w.append(df_all_.loc[i])
                    df_all_["Flag"].values[i] = 1
                    df_all_["Flag"].values[i+1] = 1
                elif sum(score)==0:
                    #print(df_all_.loc[i+1])
                    w.append(df_all_.loc[i+1])
                    df_all_["Flag"].values[i] = 1
                    df_all_["Flag"].values[i+1] = 1
                else:
                    print(df_all_)
                    w.append(df_all_.loc[i])
                    w.append(df_all_.loc[i+1])
                    df_all_["Flag"].values[i] = 1
                    df_all_["Flag"].values[i+1] = 1
                #df_all_=df_all_[df_all_["Flag"]==0]
                #df_all_.reset_index()

                i+=1  

    df_w = pd.DataFrame(data = w, columns=("ID","Player","Tm","TRB","AST","BLK","STL","PTS","Summary")).drop_duplicates()
    df_w["Flag"]=0
    df_w=df_w[df_w["Summary"]!=0]
    df_w_=df_w.copy(deep=True)
    print(df_w) 
    print (df_w[0:k])
    
    for i in range(len(df_w_)):
        df_w=df_w[df_w["Flag"]==0]
        
        df_w_=df_w_.sort_values(["TRB","AST","BLK","STL","PTS"],ascending=False)  
        #df_w_.reset_index()
        for j in range(len(df_w)):
            
            df_w=df_w.sort_values(["TRB","AST","BLK","STL","PTS"],ascending=False)  
            #df_w.reset_index()
            print("df_w is: ",df_w)
            print("df_w_ is: ",df_w_)
            print(len(df_w[df_w["Flag"]==0]))
            
            score_=[]
            for ti in input_array:
                input_type_=types[ti-1]
                if df_w[input_type_].values[j]>=df_w_[input_type_].values[i]:
                    score_.append(1)
                else:
                    score_.append(0)  
            

            if sum(score_)==len(input_array):
                df_w_["Flag"].values[i] = 1
                print("test is: ",len(df_w),j,i,sum(score_))
            elif sum(score_)==0:
                #print("test is: ",len(df_w),j,df_w.loc[j])
                
                print(i,sum(score_))
                df_w["Flag"].values[j] = 1
            else:
                continue  
                
            j+=1
        i+=1
     
    df_w=df_w[df_w["Flag"]==0]
    df_w=df_w.sort_values("Summary",ascending=False)


    print(df_w)
    print (df_w[0:k])
    df_w.to_csv(output_alias+str(input_array)+"Not Nominated Players"+data_extension)

    f=open (log_alias+"log.txt","a")
    f.write("--------Assigment 3 Q2: Skyline------------\n")
    f.write("The top k of the players based on Skyline Algorithm is:{} \n".format(df_w[0:k]))
    f.close()

    return df_w                      

    
if __name__=="__main__":
    input_array = np.loadtxt(input_alias+data_array+file_type,dtype=int,delimiter=",")
    print(input_array)
    k = int(np.loadtxt(input_alias+data_k+file_type,dtype=int,delimiter=","))
    print(k)
    folder_path = output_alias
    if not os.path.exists(folder_path):
        os.mkdir(output_alias)
    benchmark(input_array,k)
    mySkyline(input_array,k)
    myNRA(input_array,k)

    
    




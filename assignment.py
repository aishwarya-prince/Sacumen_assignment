def create_dic(a,b):
    dic[a]= b

def dictionary_creator(given_string):   
    #to remove data before cat key
    pos_cat=  given_string.find("cat")

    #to locate from msg key starts and ends position in string
    pos_msg= given_string.find("msg")
    pos_host = given_string.find("dhost")

    #creating list by spliting strings based on msg position
    first_list= given_string[pos_cat:pos_msg].split(" ")
    second_list = given_string[pos_msg: pos_host].split(" ")
    third_list = given_string[pos_host:].split(" ")

    #create list , which contains all the 3 lists
    new_list =[first_list,second_list, third_list]

    for i in range(0,len(new_list)):
        #condition to allow only first_list and second_list
        if i==0 or i ==2:
            for j in new_list[i]:
                sub_list = j.split("=")
                len_sublist = len(sub_list)

                #if len_sublist is 2, than key value pair is formed easily
                if len_sublist==2:
                    create_dic(sub_list[0],sub_list[1])

                #if len_sublist is greater than 2, then its link spliting to pecies due to presence of "="
                elif len_sublist> 2:
                    b = ""
                    #cs2 and cs4 has link as value , so concatenating it
                    if sub_list[0]== "cs2" or sub_list[0]== "cs4":
                            for i in sub_list[1:]:
                                if b=="":
                                    b=b+i
                                else:
                                    b = b+"="+i
                    else:
                        print("its not cs2 or cs4")
                    create_dic(sub_list[0],b)

        #this is msg list, broken into peices due to presence of space
        else:
            msg_list =given_string[pos_msg: pos_host].split('=')
            b=""
            #so concatenating it
            for i in msg_list[1:]:
                if b=="":
                    b=b+i
                else:
                    b=b+"="+i
            create_dic(msg_list[0],b)  

    print(dic)  

dic = {}
given_string ="SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1"
dictionary_creator(given_string)

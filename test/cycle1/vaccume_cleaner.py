pri_room=input("enter the room the agent is present in(A/B)")
pri_status=int(input("enter the status of the room (0-clean,1-dirty)"))
sec_status=int(input("enter the status of other room"))

cost=0

if pri_room in ['A','a']:
    print("agent starting in room A")
    print(f"current status {pri_status}")
    if pri_status==1:
        print("cleaning cost =1")
        cost+=1

        if sec_status==1:
            print("room B is dirty moving to room B cost=1")
            cost+=1
            print("cleaning")
            cost+=1

        else:
            print("room B is also clean no action")

    
    else:
        print("room A is clean no action")
        
        if sec_status==1:
            print("room B is dirty moving to room B cost=1")
            cost+=1
            print("cleaning")
            cost+=1
        else:
            print("room B is also clean no action")
            
else:
    print("agent starting in room ",pri_room)
    print(f"current status {pri_status}")
    if pri_status==1:
        print("cleaning cost =1")
        cost+=1

        if sec_status==1:
            print("room A is dirty moving to room B cost=1")
            cost+=1
            print("cleaning")
            cost+=1

        else:
            print("room A is also clean no action")

    
    else:
        print("room B is clean no action")
        
        if sec_status==1:
            print("room A is dirty moving to room B cost=1")
            cost+=1
            print("cleaning")
            cost+=1
        else:
            print("room A is also clean no action")
    
print(f"total cost for cleaning={cost}")

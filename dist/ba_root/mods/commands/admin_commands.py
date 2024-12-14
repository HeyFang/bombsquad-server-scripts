import _babase
import _bascenev1

import bacommon as bac
import babase as ba
import bascenev1 as bs

def kick(args):
    client_id = args[0]
    reason = " ".join(args[1:])
    
    try:
        # time in seconds
        bs.disconnect_client(int(client_id), ban_time=60*5)
        bs.chatmessage(f"Client ({client_id}) has been kicked")
    except Exception as e:
        print("there was an error while kicking client")
        print(e)
    

def end(*args):
    print('calling end')
    print(bs.get_foreground_host_activity())
    print(bs.get_foreground_host_activity().context)

    with bs.get_foreground_host_activity().context:
        bs.get_foreground_host_activity().end_game()
        bs.chatmessage(f"Admin Command Accepted. Game End")
    
    
def list(*args):
    ros = bs.get_game_roster()
    print(ros)
    
    
def maxplayers(args):
    try:
        party_size = int(args[0])
    except TypeError:
        bs.screenmessage("Enter a valid integer limit")

    try:
        bs.set_public_party_max_size(party_size)
        bs.chatmessage(f"Max Player limit has been set to {str(party_size)}")
    except Exception as e:
        print(e)
        
        
def getmaxplayers(*args):
    bs.chatmessage(f"Max player limit is set to {str(bs.get_public_party_max_size())}")
    
    
def remove(args):
    client_id = int(args[0])
    reason = " ".join(args[1:]) or "inactive"
    ros = bs.get_game_roster()
    for player in ros:
        if player["client_id"] == client_id:
            for splayer in bs.get_foreground_host_session().sessionplayers:
                if player["players"][0]["id"] == splayer.id:
                    try:
                        splayer.remove_from_game()
                        bs.chatmessage(f"{player["players"][0]["name"]} was removed for reason: {reason}")
                    except Exception as e:
                        print(e)
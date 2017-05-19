import socket

def print_remote_machine_info():
    remote_host =  'www.siga.frba.utn.edu.asr'
    try: 
        print("Ip address: %s" %socket.gethostbyname(remote_host))
    except:
        print("%s: %s" %(remote_host, "err_msg"))
        
        
if __name__ == "__main__":
    print_remote_machine_info()

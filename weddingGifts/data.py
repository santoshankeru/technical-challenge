import json

products_list = {}
def Products():
    pListFile = 'data_files/products.json'
    with open(pListFile) as jFile :
        products_list = json.load(jFile)

    return products_list

giftLinks_list = {}
def GiftLinks():
    gLinksFile = 'data_files/gift_links.json'
    with open(gLinksFile) as jFile :
        giftLinks_list = json.load(jFile)
    
    return giftLinks_list

userData = {}
def UserAuthentication() :
    uData = 'data_files/user_auth.json'
    with open(uData) as jFile :
        userData = json.load(jFile)

    return userData

def AddGiftLinks(data):
    try:
        gLinksFile = 'data_files/gift_links.json'
        with open(gLinksFile, 'w', encoding='utf-8') as jFile :
            json.dump(data, jFile, ensure_ascii=False, indent=4)
        
        return 1
    except:
        return 0

def GetLink(id):
    link_data = GiftLinks()
    plist_data = Products()
    temp_list = []
    pid = []
    pur_id = []
    pur_list = []
    npur_list = []
    linkData = {}
    
    for item in link_data:
        if item['link_id'] == id :
            pid = [int(i) for i in item['products']]
            pur_id = [int(i) for i in item['purchases']]
            linkData['link_id'] = item['link_id']
            linkData['valid_till'] = item['valid_till']

    for prod in plist_data :
        temp_dict = prod
        if prod["id"] in set(pid) :
            temp_dict['is_checked'] = 1
        else :
            temp_dict['is_checked'] = 0
        temp_list.append(temp_dict)
    
    for prod in plist_data :
        temp_dict = prod
        if prod['id'] in set(pid) :
            if prod["id"] in set(pur_id) :
                pur_list.append(temp_dict)
            else :
                npur_list.append(temp_dict)
    
    linkData['products'] = temp_list
    linkData['purchased'] = pur_list
    linkData['npurchased'] = npur_list

    return linkData

def UpdateLink(data) :
    try:
        tmp_list = []
        link_data = GiftLinks()  
        for item in link_data:
            if item['link_id'] == data['link_id']:
                item['valid_till'] = data['valid_till']
                item['products'] = data['products']  
            tmp_list.append(item)

        gLinksFile = 'data_files/gift_links.json'
        with open(gLinksFile, 'w', encoding='utf-8') as jFile :
            json.dump(tmp_list, jFile, ensure_ascii=False, indent=4)
        return 1
    except:
        return 0 

def GetLinkProducts(id):
    link_data = GiftLinks()
    plist_data = Products()

    pur_list = []
    prd_list = []

    temp_dict = {}
    wishList = []

    for item in link_data:
        if item['link_id'] == id:
            prd_list = [int(i) for i in item['products']]
            pur_list = [int(i) for i in item['purchases']]
        
    for prd in plist_data:
        if prd['id'] in set(prd_list) :
            temp_dict = prd
            if prd['id'] in set(pur_list) :
                temp_dict['is_purchased'] = 1
            else :
                temp_dict['is_purchased'] = 0
            temp_dict['link_id'] = id + "_" + str(prd['id'])
            wishList.append(temp_dict)
    
    return wishList

def UpdatePurchase(id):
    link_data = GiftLinks()  
    link_id = id.split('_')[0]
    prd_id = id.split('_')[1]
    tmp_list = []
    for item in link_data:
        if item['link_id'] == link_id:
            item['purchases'].append(prd_id)
        tmp_list.append(item)

    gLinksFile = 'data_files/gift_links.json'
    with open(gLinksFile, 'w', encoding='utf-8') as jFile :
        json.dump(tmp_list, jFile, ensure_ascii=False, indent=4)



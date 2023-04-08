from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
#from urllib.request import urlopen

Brand_Name = []
Model_Name = []
Browse_Type =[]
Secondary_Camera = []
Resolution =[]
Display_Size =[]
Operating_System = []
Processor_Core =[]
Primary_Clock_Speed =[]
Internal_Storage =[]
RAM =[]
Primary_Camera =[]
Network_Type =[]
FM_Radio =[]
Battery_Capacity = []
Width =[]
Height =[]
Depth =[]
Weight =[]
Price = []
Rating = []

urls=[]
for i in range(1,11):
    url = f"https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&p%5B%5D=facets.type%255B%255D%3DSmartphones&page={i}"
    urls.append(url)
#print(urls)

product_urls =[]
for i in urls:
    r = requests.get(i)
    soup = BeautifulSoup(r.content,"html.parser")

    np = soup.find_all("a",attrs={'class': '_1fQZEK'})
    #print(len(np))

    for link in np:
        product_urls.append("https://www.flipkart.com"+link.get('href'))


#print(len(product_urls))
# for product_url in product_urls:
for product_url in product_urls:
    data = requests.get(product_url)
    soup = BeautifulSoup(data.text, "html.parser")
    tab = soup.find_all("table",{"class": "_14cfVK"})

    Brand_Name.append('Samsung')

    try:
        pri = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
        Price.append(pri.text)
    except AttributeError:
        Price.append("")

    try:
        rat = soup.find("div", {"class": "_3LWZlK"})
        Rating.append(rat.text)
    except AttributeError:
        Rating.append("")

    table_values = []

    for x in tab:
        use = x.find_all('tr')

        for y in use:
            dde = y.find_all('td')
            dde_val = [y.text for y in dde]

            table_values.append(dde_val)


    for i in table_values:
        if i[0]=='Model Name':
            Model_Name.append(i[1])

    res1 = any('Model Name' in sublist for sublist in table_values)
    if res1 is False:
        Model_Name.append("")

    for i in table_values:
        if i[0]=='Browse Type':
            Browse_Type.append(i[1])

    res1 = any('Browse Type' in sublist for sublist in table_values)
    if res1 is False:
        Browse_Type.append("")

    for i in table_values:
        if i[0]=='Secondary Camera':
            Secondary_Camera.append(i[1])

    res1 = any('Secondary Camera' in sublist for sublist in table_values)
    if res1 is False:
        Secondary_Camera.append("")

    for i in table_values:
        if i[0]=='Resolution':
            Resolution.append(i[1])

    res1 = any('Resolution' in sublist for sublist in table_values)
    if res1 is False:
        Resolution.append("")

    for i in table_values:
        if i[0]=='Display Size':
            Display_Size.append(i[1])

    res1 = any('Display Size' in sublist for sublist in table_values)
    if res1 is False:
        Display_Size.append("")

    for i in table_values:
        if i[0]=='Operating System':
            Operating_System.append(i[1])

    res1 = any('Operating System' in sublist for sublist in table_values)
    if res1 is False:
        Operating_System.append("")

    for i in table_values:
        if i[0]=='Processor Core':
            Processor_Core.append(i[1])

    res1 = any('Processor Core' in sublist for sublist in table_values)
    if res1 is False:
        Processor_Core.append("")

    for i in table_values:
        if i[0] == 'Primary Clock Speed':
            Primary_Clock_Speed.append(i[1])

    res1 = any('Primary Clock Speed' in sublist for sublist in table_values)
    if res1 is False:
        Primary_Clock_Speed.append("")

    for i in table_values:
        if i[0] == 'Internal Storage':
            Internal_Storage.append(i[1])

    res1 = any('Internal Storage' in sublist for sublist in table_values)
    if res1 is False:
        Internal_Storage.append("")

    for i in table_values:
        if i[0] == 'RAM':
            RAM.append(i[1])

    res1 = any('RAM' in sublist for sublist in table_values)
    if res1 is False:
        RAM.append("")

    for i in table_values:
        if i[0] == 'Primary Camera':
            Primary_Camera.append(i[1])

    res1 = any('Primary Camera' in sublist for sublist in table_values)
    if res1 is False:
        Primary_Camera.append("")

    for i in table_values:
        if i[0] == 'Network Type':
            Network_Type.append(i[1])

    res1 = any('Network Type' in sublist for sublist in table_values)
    if res1 is False:
        Network_Type.append("")

    for i in table_values:
        if i[0] == 'Battery Capacity':
            Battery_Capacity.append(i[1])

    res1 = any('Battery Capacity' in sublist for sublist in table_values)
    if res1 is False:
        Battery_Capacity.append("")

    for i in table_values:
        if i[0] == 'Width':
            Width.append(i[1])

    res1 = any('Width' in sublist for sublist in table_values)
    if res1 is False:
        Width.append("")

    for i in table_values:
        if i[0] == 'Height':
            Height.append(i[1])

    res1 = any('Height' in sublist for sublist in table_values)
    if res1 is False:
        Height.append("")

    for i in table_values:
        if i[0] == 'Depth':
            Depth.append(i[1])

    res1 = any('Depth' in sublist for sublist in table_values)
    if res1 is False:
        Depth.append("")

    for i in table_values:
        if i[0] == 'Weight':
            Weight.append(i[1])

    res1 = any('Weight' in sublist for sublist in table_values)
    if res1 is False:
        Weight.append("")

    for i in table_values:
        if i[0] == 'FM Radio':
            FM_Radio.append(i[1])

    res1 = any('FM Radio' in sublist for sublist in table_values)
    if res1 is False:
        FM_Radio.append("")

    print("product data scraped")
    time.sleep(1)



# print(len(Model_Name),Model_Name)
# print(len(Browse_Type))
# print(len(SIM_Type))
# print(len(Touchscreen))
# print(len(Display_Size))
# print(len(Operating_System))
# print(len(Processor_Core))
# print(len(Primary_Clock_Speed))
# print(len(Internal_Storage))
# print(len(RAM))
# print(len(Primary_Camera))
# print(len(Network_Type))
# print(len(Bluetooth_Support),Bluetooth_Support)
# print(len(Battery_Capacity))
# print(len(Width))
# print(len(Height))
# print(len(Depth))
# print(len(Weight),Weight)
# print(len(Price),Price)
# print(len(Rating),Rating)

df = pd.DataFrame({"Brand_Name":Brand_Name,"Model_Name":Model_Name,"Browse_Type":Browse_Type,"Secondary_Camera":Secondary_Camera,"Resolution":Resolution,
               "Display_Size":Display_Size,"Operating_System":Operating_System,"Processor_Core":Processor_Core,"Primary_Clock_Speed":Primary_Clock_Speed,
               "Internal_Storage":Internal_Storage,"RAM":RAM,"Primary_Camera":Primary_Camera,"Network_Type":Network_Type,
               "FM_Radio":FM_Radio,"Battery_Capacity":Battery_Capacity,"Width":Width,"Height":Height,"Depth":Depth,
               "Weight":Weight,"Price":Price,"Rating":Rating})

df.to_csv("samsung_data.csv", index=False)






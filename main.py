from selenium import webdriver
import re
import json
import datetime

driver = webdriver.Chrome()
driver.implicitly_wait(20)

sizes = ['40公釐','44公釐']
network_types = ['gps','行動網路']

aluminum_colors = ['銀色','金色','太空灰色']
aluminum_strap_colors = ['白色','粉沙色','黑色']
aluminum_strap_types = ['運動型錶帶','運動型錶環']

material = ['鋁金屬','不鏽鋼']

regular_version = {
    'create_time' : str(datetime.datetime.now()),
    'watch_type' : 'regular',
    'data' : []
}

nike_version = {
    'create_time' : str(datetime.datetime.now()),
    'watch_type' : 'nike',
    'data' : []
}

# 一般版本 鋁金屬
for aluminum_strap_type in aluminum_strap_types:
    for i_color in range(3):
        #運動錶環白色->貝殼白
        special_white = ''
        if aluminum_strap_type == '運動型錶環' and i_color == 0:
            special_white = '貝殼'
        
        temp = {
            'material' : material[0],
            'strap_type' : aluminum_strap_type,
            'strap_color' : special_white + aluminum_strap_colors[i_color],
            'watch_color' : aluminum_colors[i_color],
            'data' : []
        }
        for size in sizes:
            for network_type in network_types:
                
                url = size +"-"+ network_type +"-"+ aluminum_colors[i_color] +"-"+ material[0] +"-"+ special_white + aluminum_strap_colors[i_color]+"-"+ aluminum_strap_type
                print(url)
                driver.get("https://www.apple.com/tw/shop/buy-watch/apple-watch/"+ url)
                pickup_date = driver.find_element_by_xpath('//*[@id="check-availability-search-section"]/div/div/div/div/span[2]').get_attribute("innerText")
                ships_date = driver.find_element_by_xpath('//*[@id="primary"]/summary-builder/div[3]/div[1]/materializer/div[2]/div/div/ul/li[1]/span').get_attribute("innerText")
                
                #清除偶爾會出現的換行及空白字元
                pickup_date = re.sub(r'\n\s+', '', pickup_date)
                ships_date = re.sub(r'\n\s+', '', ships_date)
                print("取貨: "+pickup_date)
                print("運送: "+ships_date)
                print()

                temp_detail = {
                'size' : size,
                'network_type' : network_type,
                'pickup_date' : pickup_date,
                'ships_date' : ships_date,
                }
                temp['data'].append(temp_detail)
        regular_version['data'].append(temp)

stainless_steel_colors = ['不鏽鋼','金色','太空黑色'] 
stainless_steel_sport_strap_colors = ['白色','石色','黑色']
stainless_steel_milanese_strap_colors = ['不鏽鋼','金色','黑色']
stainless_steel_strap_types = ['運動型錶帶','米蘭式錶環']

# 一般版本 不鏽鋼
for stainless_steel_strap_type in stainless_steel_strap_types:
    for i_color in range(3):
        strap_color = ''
        if stainless_steel_strap_type == '運動型錶帶':
            strap_color = stainless_steel_sport_strap_colors[i_color]
        else:
            strap_color = stainless_steel_milanese_strap_colors[i_color]
        temp = {
            'material' : material[1],
            'strap_type' : stainless_steel_strap_type,
            'strap_color' : strap_color,
            'watch_color' : stainless_steel_colors[i_color],
            'data' : []
        }
        for size in sizes:
            url = size +"-"+ network_types[1] +"-"+ stainless_steel_colors[i_color] +"-"+ material[1] +"-" + strap_color +"-"+ stainless_steel_strap_type
            print(url)
            driver.get("https://www.apple.com/tw/shop/buy-watch/apple-watch/"+ url)
            pickup_date = driver.find_element_by_xpath('//*[@id="check-availability-search-section"]/div/div/div/div/span[2]').get_attribute("innerText")
            ships_date = driver.find_element_by_xpath('//*[@id="primary"]/summary-builder/div[3]/div[1]/materializer/div[2]/div/div/ul/li[1]/span').get_attribute("innerText")
            
            #清除偶爾會出現的換行及空白字元
            pickup_date = re.sub(r'\n\s+', '', pickup_date)
            ships_date = re.sub(r'\n\s+', '', ships_date)
            print("取貨: "+pickup_date)
            print("運送: "+ships_date)
            print()

            temp_detail = {
                'size' : size,
                'network_type' : network_type,
                'pickup_date' : pickup_date,
                'ships_date' : ships_date,
            }
            temp['data'].append(temp_detail)
        regular_version['data'].append(temp)

print(json.dumps(regular_version, ensure_ascii=False))

with open('./json/regular_version.json', 'w') as outfile:  
    json.dump(regular_version, outfile, ensure_ascii=False)

nike_colors = ['銀色','太空灰色'] 
nike_sport_band_strap_colors = ['pure-platinum-黑色','anthracite-黑色']
nike_sport_loop_strap_colors = ['雪峰白色','黑色']
nike_strap_types = ['運動型錶帶','運動型錶環']


# nike版本
for nike_strap_type in nike_strap_types:
    for i_color in range(2):
        strap_color = ''
        if nike_strap_type == '運動型錶帶':
            strap_color = nike_sport_band_strap_colors[i_color]
        else:
            strap_color = nike_sport_loop_strap_colors[i_color]
        temp = {
            'material' : material[0],
            'strap_type' : nike_strap_type,
            'strap_color' : strap_color,
            'watch_color' : nike_colors[i_color],
            'data' : []
        }
        for size in sizes:
            for network_type in network_types:

                url = size +"-"+ network_type +"-"+ material[0] +"-"+ nike_colors[i_color] +"-"+ strap_color +"-"+ nike_strap_type
                print(url)
                driver.get("https://www.apple.com/tw/shop/buy-watch/apple-watch/"+ url)
                pickup_date = driver.find_element_by_xpath('//*[@id="check-availability-search-section"]/div/div/div/div/span[2]').get_attribute("innerText")
                ships_date = driver.find_element_by_xpath('//*[@id="primary"]/summary-builder/div[3]/div[1]/materializer/div[2]/div/div/ul/li[1]/span').get_attribute("innerText")
                
                #清除偶爾會出現的換行及空白字元
                pickup_date = re.sub(r'\n\s+', '', pickup_date)
                ships_date = re.sub(r'\n\s+', '', ships_date)
                print("取貨: "+pickup_date)
                print("運送: "+ships_date)
                print()

                temp_detail = {
                    'size' : size,
                    'network_type' : network_type,
                    'pickup_date' : pickup_date,
                    'ships_date' : ships_date,
                }
                temp['data'].append(temp_detail)
        nike_version['data'].append(temp)
print(json.dumps(nike_version, ensure_ascii=False))
with open('./json/nike_version.json', 'w') as outfile:  
    json.dump(nike_version, outfile, ensure_ascii=False)

driver.close()
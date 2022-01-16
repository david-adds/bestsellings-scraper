
from dis import dis


def get_platforms(list_classes):
    platforms = []
    for item in list_classes:
        platform = item.split(' ')[-1]
        if platform=='win':
            platforms.append('Windows')
        elif platform=='mac':
            platforms.append('Mac OS')
        elif platform=='linux':
            platforms.append('Linux')
        # if platform=='vr_supported':
        else:
            platforms.append('VR Supported')
    return platforms

def clean_discount_rate(discount_rate):
    if discount_rate:
        return discount_rate.lstrip('-')
    return discount_rate

def get_original_price(selector_obj):
    original_price = ''
    div_with_discount = selector_obj.xpath(".//div[contains(@class,'search_price discounted')]")
    if len(div_with_discount) > 0:
        original_price = div_with_discount.xpath(".//span/strike/text()").get()
    else:
        original_price = selector_obj.xpath("normalize-space(.//div[contains(@class,'search_price')]/text())").get()      
    return original_price 

def clean_discounted_price(discounted_price):
    if discounted_price:
        return discounted_price.strip()
    return discounted_price
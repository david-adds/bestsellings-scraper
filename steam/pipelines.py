
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

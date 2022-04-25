text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

import re

pattern = r'\b\w{4}\b'

search = re.findall(pattern, text)
print(search)
# зачтено

text = 'https://vk.com/settings?act=change_regional&amp;hash=529d74125d44294119&amp;lang_id=3/sitemap.xml'
pattern = r'\w[^:/]+'

search = re.findall(pattern, text)
print('.'.join(search))
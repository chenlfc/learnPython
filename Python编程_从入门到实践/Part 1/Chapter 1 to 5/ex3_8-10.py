# create by o.c. 2018/7/19

sites = ['united states', 'england', 'japan', 'venice', 'mexico']
print('原始的列表\t\t', sites)
print('临时排序后的列表\t', sorted(sites))
print('原始的列表\t\t', sites)
print('临时反向排序后的列表\t', sorted(sites, reverse=True))
print('原始的列表\t\t', sites)
sites.reverse()
print('反转顺序后的列表\t', sites)
sites.reverse()
print('再次反转后还原的原始列表', sites)
sites.sort()
print('排序后的列表\t\t', sites)
sites.sort(reverse=True)
print('逆向排序后的列表\t', sites)

sitemap = ['s上海', 'b北京', 'g广州', 'w武汉', 'g贵州', 'c常州', 'n宁波']
print(sitemap)
print(sorted(sitemap))
print(sorted(sitemap, reverse=True))
sitemap.reverse()
print(sitemap)
sitemap.reverse()
print(sitemap)
sitemap.sort()
print(sitemap)
sitemap.sort(reverse=True)
print(sitemap)

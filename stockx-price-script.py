import webbrowser

def open_link_with_variable(link, sku_list):
    for variable in sku_list:
        full_link = link + variable
        webbrowser.open(full_link, new=2)

link = "https://stockx.com/search?s="
variable = input("Input your designated SKU(s) separated by commas: ").split(",")
full_link = link + variable[0]
webbrowser.open(full_link, new=2)

open_link_with_variable(link, variable)
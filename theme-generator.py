import colorsys

def clamp(x):
    return max(0, min(x, 255))

def hex_to_hsl(hex):
    r, g, b = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    return h, l, s

def find_interval(l):
    l = l * 100
    toBlack = (100 - l) /10
    toWhite = l / 10
    intervals = []
    
    i = 0
    while i < 100:
        if i < l:
            i += toWhite
        elif i >= l:
            i += toBlack

        intervals.append(round(i))
    
    return intervals

def generate_pallete(hex):
    hsl = hex_to_hsl(hex)
    interval = find_interval(hsl[1])
    pallete = []
    for i in interval:
        r, g, b = colorsys.hls_to_rgb(hsl[0], i/100, hsl[2])
        pallete.append("#{0:02x}{1:02x}{2:02x}".format(clamp(int(r * 255)), clamp(int(g * 255)), clamp(int(b * 255))))
    return pallete

def generate_theme(colors):
    for color, hex in colors.items():
        pallete = generate_pallete(hex)
        colors[color] = pallete
    return colors

def format_pallete(pallete):
    result = {}
    i = 100
    for color in pallete:
        result[i] = color
        i += 100

    string = ''

    for key, value in result.items():
        string += f'\t\t{key}:' + "'" + f'{value}' + "',\n"

    return string

def format_theme(theme, name):
    string = f'{name}: '+ "{\n"
    for key, value in theme.items():
        string += f'\t{name}_{key}: '+ "{" + f' \n {format_pallete(value)}' + "\t},\n"
    string += '}'
    return string

def save_theme(name, colors):
    f = open(f'{name}.scss', 'w')
    theme = generate_theme(colors)
    theme = format_theme(theme, name)
    f.write(theme)

def main():
    print('Welcome to the SCSS theme generator!\n')
    print("What is the name of your theme?")
    theme = input("Theme name: ")

    print("How many colors do you want in your pallete?")
    colornum = int(input())
    colors = {}
    for i in range(colornum):
        colorname = input(f'Name of the {i+1} color: ')
        h = input(f'Hex of the {i+1} color: ').lstrip('#')
        colors[colorname] = h
    
    save_theme(theme, colors)

testinput = [
    "twilight",
    "8",
    "red",
    "#CF6A4C",
    "dyellow",
    "#CDA869",
    "yellow",
    "#F9EE98",
    "green",
    "#8F9D6A",
    "lblue",
    "#AFC4FB",
    "dblue",
    "#7587A6",
    "purple",
    "#9B859D",
    "brown",
    "#9B703F"
]
main()

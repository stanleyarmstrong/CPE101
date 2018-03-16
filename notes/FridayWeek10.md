# Friday Week 10

There's office hours on Monday from 2:00pm - 3:00 pm

The final will have print statements from either Python 2 or Python 3

## Project 6

### Part 2

**Command Line Argument**

python spot_blur.py filename  rowc colc radius [reach]


Either 5 or 6 command line arguments

sys.argv
```Python

if not 4 < len(sys.argv) < 6:
    print error message
    return

filename, row_c, col_c, radius, reach = getParameter(sys.argv[1:])

width, height, color_depth, image = read_image(fin)

image = [[], [], [], [], ...] #elements are pixels
height = len(image)
width = len(image[i])

```

Image is a list of lists

Blurring an image:


Blur Completely:

for each pixel replace the values of ('r', 'g', 'b')
by ('rf', 'gf', 'bf') - the average of the color components in the surrounding

```Python

r = 1/y(r[row-1, col-1] + r[row-1][col] + r[row-1][col+1]+ r[row][col-1]+ ...)

reach = 1

def get_fully_blurred_pixel(image, r, c, reach):
    cols = [0, 0, 0]
    count = 0
    for y in range(r- reach, r + reach + 1):
        if 0 <= y < len(image):
            for x in range(c - reach, c + reach + 1):
                if 0 <= x < len(image[0]):
                        count += 1
                        cols[0] = cols[0] + image[y][x].r
                        cols[1] = cols[1] + image[y][x].g
                        cols[2] = cols[2] + image[y][x].b
    return Pixel(int(cols[0]/count), int(cols[1]/count), int(cols[2]/count))
                        
```

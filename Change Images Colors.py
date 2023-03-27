from PIL import Image
from os import listdir
from os.path import isfile, join

def ChangeImageColor (A,B,path,newPath,openImage):
    """
    Replace pixels with A color with the B color
    if A is empty, it replace all which is not colorless with B color
    if newPath is empty newPath = copy-"path"
    work only with PNG
    empty is if the value is : () or ""
    
    
    Parameters
    ----------
    A : tuple, (Red, Green, Blue) or () 
    Color to replace
    
    B : tuple, (Red, Green, Blue)
    Color to put
    
    path : image path
    
    newPath : new image path
    
    openImage : did you want to open the edited image


    Returns
    -------
    None

    """
    try:
        if path[len(path)-4:] != ".png":
            print("ERROR path must be PNG")
            return None
        img = Image.open(str(path))
        if A == False or A == ""or A == ():
            r1 = -1
        else :
            r1,g1,b1=A
        r2,g2,b2=B
        x,y=0,0
        w,h = img.width,img.height
        for y in range (h):
            for x in range (w):
                r,g,b,a=img.getpixel((x,y))
                if r1 == -1 :
                    if a!=0:
                        img.putpixel((x,y),(r2,g2,b2,a))
                else:
                    if r ==r1 and g==g1 and b==b1:
                        img.putpixel((x,y),(r2,g2,b2,a))
        if openImage:
            img.show()
        if newPath == "" or newPath == ():
            newPath = "copy-"+str(path)
        img.save(newPath)
    except FileNotFoundError:
        print("there is no image at this location")
    except :
        print("something went wrong:(")

def ChangeImagesColor(A,B,path,prefix,openImage):
    """
    Replace pixels with A color with the B color (for all the png of the file)
    if A is empty, it replace all which is not colorless with B color
    if prefix is empty newPath = copy-"path"
    work only with PNG
    empty is if the value is : () or ""
    
    
    Parameters
    ----------
    A : tuple, (Red, Green, Blue) or () 
    Color to replace
    
    B : tuple, (Red, Green, Blue)
    Color to put
    
    path : image path
    
    prefix : prefix for the new image name
    
    openImage : did you want to open the edited images
    

    Returns
    -------
    None.

    """
    try :
        image=[]
        fichiers = [f for f in listdir(path) if isfile(join(path, f))]
        for f in fichiers:
            if f[len(f)-4:]== ".png":
                image.append(f)
        if prefix == "" or prefix == () :
            prefix = "copy-"
        for i in image :
            newPath = str(path)+"/"+str(prefix)+str(i)
            pathI = str(path)+"/"+str(i)
            print(pathI)
            ChangeImageColor(A,B,pathI,newPath,openImage)
    except:
        print("something went wrong:(")
        
def ChangeImageColors(A,B,path,prefix,openImage):
    """
    Replace pixels with A color with the B colors with as many color as you want
    if A is empty, it replace all which is not colorless with B color
    if prefix == True -> prefix will be the color tag
    else -> prefix will be 1,2,3....n
    work only with PNG
    empty is if the value is : () or ""
    
    
    Parameters
    ----------
    A : tuple, (Red, Green, Blue) or () 
    Color to replace
    
    B : tuple, [(Red, Green, Blue),...,(Red, Green, Blue)]
    Colors to put
    
    path : image path
    
    prefix : image prefix
    
    openImage : did you want to open the edited images


    Returns
    -------
    None

    """
    try :
        print(prefix)
        if not prefix:
            pre1 = 1
        for color in B:
            print(prefix)
            if prefix == True :
                print("error")
                pre = str(color[0])+"-"+str(color[1])+"-"+str(color[2])+"-"
            if not prefix:
                pre = str(pre1)+"-" 
            newPath = str(pre)+str(path)
            ChangeImageColor(A,color,path,newPath,openImage)
            if not prefix:
                pre1 +=1
    except:
        print("something went wrong:(")
        
def ChangeImageSize(path,prefix,north,south,east,west,openImage):
    """
    Change the size of an image
    if prefix is empty newPath = copy-"path"
    work only with PNG or JPG
    empty is if the value is : () or ""

    Parameters
    ----------
    path : image path
    
    prefix : image prefix
    
    north : how many pixels did you want to delete on north
    
    south : how many pixels did you want to delete on south
    
    east : how many pixels did you want to delete on east
    
    west : how many pixels did you want to delete on west
    
    openImage : did you want to open the edited image

    Returns
    -------
    None.

    """
    try:
        png = isPng(path)
        jpg = isJpg(path)
        img = Image.open(str(path))
        T1= []
        T2=[]
        w,h = img.width,img.height
        if north+south >= h:
            print("ERROR you can't delete more pixel the the image is")
            return None
        elif west+east >= w:
            print("ERROR you can't delete more pixel the the image is")
        elif north==0 and south==0 and east==0 and west==0:
            print("ERROR you can't delete any pixel")
            return None
        for y in range (h):
            T= []
            for x in range (w):
                if png:
                    r,g,b,a=img.getpixel((x,y))
                    color = (r,g,b,a)
                if jpg:
                    r,g,b=img.getpixel((x,y))
                    color = (r,g,b)
                T.append(color)
            T1.append(T)
        
        T1=T1[north:h-south]
        for t in T1 :
            t=t[west:w-east]
            T2.append(t)
            
        y,x=h-south-north,w-east-west
        coord = (x,y)
        print(coord,"coord ?")
        if png:
            print("png")
            img2 = Image.new('RGBA', coord)
        elif jpg:
            print("jpg")
            img2 = Image.new('RGB', coord)
        else:
            print("ERROR something went wrong we need jpg or png")
            
        w,h = img2.width,img2.height
        print(h,w,len(T2),len(T2[0]))
        
        
        for y in range (h):
            for x in range (w):
                #print(x,y)
                color = T2[y][x]
                #print(color)
                if png:
                    if color[3]!=0:
                        img2.putpixel((x,y),color)
                if jpg:
                    img2.putpixel((x,y),color)
        if openImage :
            img2.show()
        if prefix == "" or prefix == ():
            newPath = "copy-"+str(path)
        else :
            newPath = prefix+str(path)
        img2.save(newPath)
    except FileNotFoundError:
        print("there is no image at this location")
    #except:
        #print("something went wrong:(")
        
def isPng(path):
    if path[len(path)-4:] == ".png":
        return True
    return False
def isJpg(path):
    if path[len(path)-4:] == ".jpg":
        return True
    return False

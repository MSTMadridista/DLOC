import re
import webbrowser
import sys
import time
import os
os.system("")

########################################################color_codes######################################################################

R = '\033[38;2;255;0;43m'
G = '\033[38;2;2;219;111m'
B = '\033[38;2;51;18;255m'
C = '\033[38;2;51;241;255m'
W = '\033[38;2;245;245;245m'
P = '\033[38;2;171;94;180m'
G2 = '\033[38;2;63;184;67m'
L = '\033[38;2;132;119;140m'
O = '\033[38;2;255;166;0m'
BL = '\033[38;2;128;125;120m'
G3 = '\033[38;2;0;255;0m'

########################################################funcs#######################################################################

def extract_class_token(link):
    pattern = r"(?<=shirazu.ac.ir/)(.*?)(?=/|\?)"
    match = re.search(pattern, link)

    if match:
        return match.group(1)
    else:
        invalid_link_msg = f""" {R} \nInvalid link provided! Please check and try again. {W}

"""
        for char in invalid_link_msg:
          sys.stdout.write (char)
          sys.stdout. flush ()
          time.sleep(0.05) 

        sys.exit(-1)

def validate_year(year):
    if year.startswith("4") and len(year) == 3:
      year="1"+year    
    if not year.isdigit():
        invalid_y_ft = f'''{R}\nInvalid year format!{W}
'''
        sys.exit(-1)
    if int(year) < 1382 :
        invalid_y_msg= f'''{R}\nInvalid year! {W} 

'''
        for char in invalid_y_msg:
          sys.stdout.write (char)
          sys.stdout. flush ()
          time.sleep(0.05)
        sys.exit(-1)
    return year

def validate_semester(semester):
  valid_semesters = ["1", "2"]
  if semester not in valid_semesters:
    Invalid_semester_msg = f'''{R}\nInvalid semester. Please use '1' or '2' 
'''
    for char in Invalid_semester_msg:
          sys.stdout.write (char)
          sys.stdout. flush ()
          time.sleep(0.05)
    time.sleep(1)
    Invalid_semester_msg2=f'''! Attention: Please choose a valid semester.{W}
'''
    for char in Invalid_semester_msg2:
          sys.stdout.write (char)
          sys.stdout. flush ()
          time.sleep(0.05)
    time.sleep(1)
    sys.exit(-1)
  return semester


########################################################and here we go :)###########################################################

banner = f'''
  {L}-{P}={BL}%1010001011{P}.{L}-   {L}-{G2}*0{BL}0010{P}1=--{L}-      {L}-{P}--{BL} 1010011101{P}={L}-   {L}-{P}-{G2}:{BL} 00101011101{P}={L}-       {P}--{W}##101*:{L}:
{G2}--=={BL}0010101010101{P}--  {G2}-+{BL}0001{P}1=--        {G2}--{BL}101010101101{P}-  {G2}  -+{BL}0101010110101{P}=     {G2} --{W}%0+:  -=**11{P}--
{G2}  --{BL}1111{P}+* {G2}*++{BL}0000{P}-={G2}-=+{BL}0011{P}0=        {G2} --{BL}0100 {P}***{G2}*={BL}0101{P}={L}- {G2} ={BL}0101{P}+--------    {G2}  --{W}10{P}:+    {G2} =-{W}01%1={P} ..    
{G2}-==#{BL}0001{P}=  {G2} -+#{BL}10110{P}-{G2} %{BL}0001{P}1= {G2} ---====%{BL}0101{P}-=     *{BL}101%{G2}*--{BL}111#{P}-- {G2}      ---===={W}+0::        {G2}---={W}1++001%{P}-- 
  {P} +{BL}1111{P}==--  -+{BL}10101{P}={G2}%{BL}00001{P}---   {G2} --={BL}0101{P}==---   {G2} +{BL}0101{P}-{BL}0111{P}+=--      {G2}    -={W}%11{P}=--- {L}  -{W}1111{L}+    {P}+{W}0101:{P}==---- 
   ={BL}0110{G2}+--  {P} ={BL}00011{G2}={P}-%{BL}00011{G2}-       {P} ++{BL}1100{G2}==- {P}  =={BL}0010{G2}%={P}-{BL}1101{G2}=+------      {P} -{W}001{G2}---   {L}-{W}1101{L}-    {P} ={W}-00= 
 {P}  ={BL}1110{G2}*+----{BL}10101{G2}=--{P}*{BL}00110{G2}+++++==-{P} --={BL}0101{G2}=+=++{P}+{BL}0001{G2}%= {P} ={BL}0101{G2}$=++++++=- {P} --{W}100{G2}-=- {W}  <110010> {P} =+{W}11{G2}*:==-- 
{P}---=1{BL}1001101001111{G2}-{P} ---1{BL}100101010110{P}:: -:{BL}010101011101{G2}#{P} --==:{BL}1110110010010{G2};{P}----={W}000     \\1010/   {P}-{W}101
 {P}  =%{BL}10101100101{P}=--   -0{BL}101011001010{G2}-- {P}  ={BL}1101011010{G2}*.  {P}   =={BL}010101001100{G2}-      {P}-{W}0%0    \\10/   %$&{G2}=
        ---=--             -------           -----            -------              {W}      \\/                                                                       
'''

for char in banner:
  sys.stdout.write (char)
  sys.stdout. flush ()
  time.sleep(0.0000001) 
time.sleep(0.5)

author = f'''
                                    {W} _          {G3}   __  __ ____ _____ 
                                    {W}| |__  _   _ {G3} |  \\/  / ___|_   _|
                                {W}    | '_ \\| | | | {G3}| |\\/| \\___ \\ | |  
                                 {W}   | |_) | |_| | {G3}| |  | |___) || |  
                                 {W}   |_.__/ \\__, | {G3}|_|  |_|____/ |_|  
                                 {W}          |___/                    
      
'''
for char in author:
  sys.stdout.write (char)
  sys.stdout. flush ()
  time.sleep(0.00000000000000000000000011) 

time.sleep(0.7)
link = input(R + "┌─[" + G + "Enter the class link" + R +"""]
└──╼ """ + B )

class_token = extract_class_token(link)

year = input( R + "┌─["+ G + "Enter the year" + R +"""]
└──╼ """  + C )
year = validate_year(year)

semester = input(R + "┌─[" + G + "Enter the semester (1/2)" + R +"""]
└──╼ """  + C )
semester = validate_semester(semester)

offline_link = "https://offline.shirazu.ac.ir/" + year + semester + "/" + class_token + ".zip"

print( O + """

Processing""", end="", flush=True)
for _ in range(4):
  time.sleep(0.7)
  print(".", end="", flush=True)
print("\n\n" + W , flush=True)


webbrowser.open(offline_link)


# Coded by MST :)

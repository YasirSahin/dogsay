import sys

if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
else:
   text = input()

lenText = len(text)

print(f"""
 ___{lenText*"_"}     
< {text} >
 ---{lenText*"-"}    
   \       ,_____ ,
    \     ,._ ,_. 7\\
     \   j `-'     /
         |o_, o    \\
        .`_y_`-,'   !
        |/   `, `._ `-,
        |_     \   _.'*\\
          >--,-'`-'*_*'``---.
          |\_* _*'-'         '
         /    `               \\
         \.         _ .       /
          '`._     /   )     /
           \  |`-,-|  /c-'7 /
            ) \ (_,| |   / (_
           ((_/   ((_;)  \_)))  
""")

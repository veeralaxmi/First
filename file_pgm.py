def main():
    line_num = 0
    file=open("C:\\Users\\rajas\\Downloads\\Veera\\project\\myfile.txt","r")
    lines=file.readlines()
    for line in lines:
        line_num +=1
        if (line_num%10 ==0):
            print(line)

if __name__ == "__main__":
    main()
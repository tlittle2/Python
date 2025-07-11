#Accepted, but not all cases pass
def main():
    d = {}
    curr_dir_files= set()
    cur_dir_name = ""

    def unload():
        d[cur_dir_name] = [i for i in curr_dir_files]
        curr_dir_files.clear()

    for _ in range(int(input())):
        #print(curr_dir)
        ip = input().split(" ")
        if ip[0] == 'cd':
            unload()
            cur_dir_name = ip[1]
        else:
            curr_dir_files.add(ip[1])

    unload()

    newD = dict(filter(lambda item: len(item[1]) > 0, d.items()))
    #print(newD)

    for k,v in sorted(newD.items()):
        for i in sorted(v):
            print("git add {}{}".format(k if k == "" else k +"/", i))

    print("git commit")
    print("git push")

if __name__ == "__main__":
    main()

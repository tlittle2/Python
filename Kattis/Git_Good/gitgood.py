#Accepted, but not all cases pass
def main():
    d = {}
    curr_dir= set()

    def unload():
        d[cur_dir] = [i for i in curr_dir]
        curr_dir.clear()

    cur_dir = ""
    for _ in range(int(input())):
        #print(curr_dir)
        ip = input().split(" ")
        if ip[0] == 'cd':
            unload()
            cur_dir = ip[1]
        else:
            curr_dir.add(ip[1])

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

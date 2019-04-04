def mk_secret_map(arr1, arr2):
    result = []
    for (first_val, second_val) in zip(arr1, arr2):
        result.append(bin(first_val | second_val)[2:].replace("0", " ").replace("1", "#"))
    return result


def mk_map(map_size):
    arr = []
    while len(arr) is not map_size:
        try:
            arr.append(int(input("비밀지도의 암호를 차례대로 입력해주세요 : ")))
        except ValueError as e:
            print("")
            print("잘못된 입력입니다. 암호를 다시한번 확인하고, 숫자를 입력해주세요")
            print("")
    return arr


def get_map_size():
    while True:
        try:
            map_size = int(input("프로도가 갖고 있는 비밀지도의 크기는? "))
            break
        except ValueError as e:
            print("")
            print("비밀지도의 크기는 숫자에요!!")
            print("")
    return map_size


def main():
    print("{}".format("*"*30))
    print("비밀지도를 해독합니다!!")

    map_size = get_map_size()

    print("{}".format("*"*30))
    print("첫 번째 비밀지도를 입력합니다.")
    arr1 = mk_map(map_size)

    print("{}".format("*"*30))
    print("두 번째 비밀지도를 입력합니다.")
    arr2 = mk_map(map_size)

    result = mk_secret_map(arr1, arr2)

    print("{}".format("*"*30))
    print("네오가 비밀지도를 완성했어요!!")

    for i in result:
        print(i)



if __name__ == "__main__":
    main()

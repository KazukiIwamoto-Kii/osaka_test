spot_list = { 0 : "海遊館",
            1 : "万博公園",
            2 : "USJ",
            3 : "なんば",
            4 : "梅田",
            5 : "天王寺",
            6 : "長居公園",
            7 : "大阪城",
            8 : "新世界",
            9 : "天王寺動物園",
            10 : "スパワールド 世界の大温泉",
            11 : "梅田スカイビル 空中庭園展望台",
            12 : "なんばグランド花月",
            13 : "なんばパークス",
            14 : "アメリカ村",
            15 : "大阪天満宮",
            16 : "四天王寺",
            17 : "住吉大社",
            18 : "国立国際美術館",
            19 : "大阪市立科学館",
            20 : "関西国際空港",
            21 : "りんくうアウトレット",
            22 : "泉南りんくう公園",
            23 : "中之島公園",
            24 : "造幣博物館",
            25 : "空庭温泉 OSAKA BAY TOWER", 
            26 : "生野コリアンタウン",
            27 : "エキスポシティ",
            28 : "ひらかたパーク",
            29 : "堺・緑のミュージアム ハーベストの丘"}


# 所要時間
syoyouzikan = [180, 120, 480, 60, 120, 60, 60, 90, 30, 150, 360, 60, 150, 60, 60, 30, 90, 30, 60, 90, 30, 240, 150, 30, 90, 240, 60, 90, 300, 180] 

# 優先度
p = [4, 3, 2, 9, 5, 8, 1, 1, 7, 5, 3, 4, 2, 1, 5, 8, 9, 2, 1, 3, 6, 8, 3, 4, 5, 2, 4, 6, 7, 8] #priority(人気度)

distance = [
    [ 0, 80, 40, 35, 35, 40, 60, 40, 40, 40, 40, 45, 50, 50, 40, 40, 40, 50, 40, 40, 90, 90, 90, 40, 50, 20, 50, 80, 70, 90],
    [80,  0, 70, 50, 50, 60, 70, 70, 60, 60, 60, 50, 60, 60, 60, 50, 70, 80, 70, 70, 120, 120, 120, 70, 60, 70, 70, 5, 70, 120],
    [40, 70,  0, 30, 20, 30, 40, 40, 20, 30, 20, 30, 30, 30, 30, 30, 30, 40, 30, 30, 70, 70, 80, 30, 40, 20, 40, 70, 70, 90],
    [35, 50, 30,  0, 10, 10, 20, 30, 20, 10, 10, 20,  5,  5, 10, 20, 20, 30, 20, 20, 50, 60, 60, 20, 30, 30, 30, 60, 50, 70],
    [35, 50, 20, 10,  0, 20, 30, 30, 20, 30, 25, 10, 15, 15, 15, 10, 20, 30, 15, 15, 60, 75, 75, 15, 25, 15, 35, 45, 45, 80],
    [40, 60, 30, 10, 20,  0, 10, 25, 10, 15, 10, 30, 15, 15, 15, 15, 10, 20, 25, 25, 50, 60, 60, 25, 30, 15, 20, 60, 60, 65],
    [60, 70, 40, 20, 30, 10,  0, 40, 20, 20, 35, 55, 40, 40, 40, 50, 35, 30, 50, 50, 80, 75, 100, 50, 60, 45, 45, 90, 75, 80],
    [40, 70, 40, 30, 30, 25, 40,  0, 50, 40, 45, 45, 40, 50, 45, 30, 45, 60, 45, 45, 100, 90, 105, 30, 40, 40, 40, 90, 60, 100],
    [40, 60, 20, 20, 20, 10, 20, 50,  0,  5,  5, 40, 25, 25, 25, 30, 30, 25, 35, 35, 60, 60, 70, 25, 35, 25, 35, 75, 60, 75],
    [40, 60, 30, 10, 30, 15, 20, 40,  5,  0,  5, 40, 25, 20, 25, 25, 25, 25, 35, 35, 60, 60, 75, 25, 35, 20, 30, 75, 60, 75],
    [40, 60, 20, 10, 25, 10, 35, 45,  5,  5,  0, 40, 25, 25, 25, 30, 30, 25, 35, 35, 60, 60, 70, 25, 35, 25, 35, 75, 60, 75],
    [45, 50, 30, 20, 10, 30, 55, 45, 40, 40, 40,  0, 30, 40, 30, 30, 45, 50, 30, 30, 90, 85, 95, 30, 35, 25, 45, 65, 60, 100],
    [50, 60, 30,  5, 15, 15, 40, 40, 25, 25, 25, 30,  0,  5, 15, 20, 40, 25, 30, 35, 65, 60, 65, 20, 30, 30, 30, 65, 55, 75],
    [50, 60, 30,  5, 15, 15, 40, 50, 25, 20, 25, 40,  5,  0, 15, 35, 35, 30, 30, 35, 60, 65, 70, 25, 40, 30, 35, 75, 60, 70],
    [40, 60, 30, 10, 15, 15, 40, 45, 25, 25, 25, 30, 15, 15,  0, 25, 35, 35, 30, 30, 65, 65, 80, 25, 35, 35, 35, 70, 55, 80],
    [40, 50, 30, 20, 10, 15, 50, 30, 30, 25, 30, 30, 20, 35, 25,  0, 30, 35, 25, 25, 75, 70, 85, 15, 20, 30, 40, 60, 45, 90],
    [40, 70, 30, 20, 20, 10, 35, 45, 30, 25, 30, 45, 40, 35, 35, 30,  0, 35, 45, 45, 70, 70, 85, 35, 40, 30, 30, 80, 60, 85],
    [50, 80, 40, 30, 30, 20, 30, 60, 25, 25, 25, 50, 25, 30, 35, 35, 35,  0, 50, 50, 60, 60, 65, 40, 50, 40, 50, 90, 75, 80],
    [40, 70, 30, 20, 15, 25, 50, 45, 35, 35, 35, 30, 30, 30, 30, 25, 45, 50,  0,  5, 90, 90, 95, 35, 35, 25, 50, 65, 50, 100],
    [40, 70, 30, 20, 15, 25, 50, 45, 35, 35, 35, 30, 35, 35, 30, 25, 45, 50,  5,  0, 90, 90, 95, 35, 35, 25, 50, 65, 50, 100],
    [90, 120, 70, 50, 60, 50, 80, 100, 60, 60, 60, 90, 65, 60, 65, 75, 70, 60, 90, 90, 0, 20, 50, 85, 100, 70, 85, 125, 120, 110],
    [90, 120, 70, 60, 75, 60, 75, 90, 60, 60, 60, 85, 60, 65, 65, 70, 70, 60, 90, 90, 20, 0, 35, 80, 95, 80, 90, 125, 120, 100],
    [90, 120, 80, 60, 75, 60, 100, 105, 70, 75, 70, 95, 65, 70, 80, 85, 85, 65, 95, 95, 50, 35, 0, 90, 120, 80, 95, 140, 130, 130],
    [40, 70, 30, 20, 15, 25, 50, 30, 25, 25, 25, 30, 20, 25, 25, 15, 35, 40, 35, 35, 85, 80, 90,  0, 30, 30, 50, 70, 40, 100],
    [50, 60, 40, 30, 25, 30, 60, 40, 35, 35, 35, 35, 30, 40, 35, 20, 40, 50, 35, 35, 100, 95, 120, 30, 0, 40, 40, 70, 45, 105],
    [20, 70, 20, 30, 15, 15, 45, 40, 25, 20, 25, 25, 30, 30, 35, 30, 30, 40, 25, 25, 70, 80, 80, 30, 40,  0, 40, 65, 60, 80],
    [50, 70, 40, 30, 35, 20, 45, 40, 35, 30, 35, 45, 30, 35, 35, 40, 30, 50, 50, 50, 85, 90, 95, 50, 40, 40,  0, 80, 60, 100],
    [80,  5, 70, 60, 45, 60, 90, 90, 75, 75, 75, 65, 65, 75, 70, 60, 80, 90, 65, 65, 125, 125, 140, 70, 70, 65, 80, 0, 90, 160],
    [70, 70, 70, 50, 45, 60, 75, 60, 60, 60, 60, 60, 55, 60, 55, 45, 60, 75, 50, 50, 120, 120, 130, 40, 45, 60, 60, 90, 0, 135],
    [90, 120, 90, 70, 80, 65, 80, 100, 75, 75, 75, 100, 75, 70, 80, 90, 85, 80, 100, 100, 110, 100, 130, 100, 105, 80, 100, 160, 135, 0]
    ]



print(len(p))
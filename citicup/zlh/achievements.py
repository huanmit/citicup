from django.db import connection


# 8.餐具收藏家 #
def chop_collector(userID: str):
    res = 0
    if third_chop(userID):
        res += 1
    if second_chop(userID):
        res += 1
    if first_chop(userID):
        res += 1
    return res  # res为1：餐具收藏家（铜），2:银，3:金

# 累计上传50次


def third_chop(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=3 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 50:
        res = True
    return res


# 累计上传100次
def second_chop(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=3 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 100:
        res = True
    return res

# 累计上传200次


def first_chop(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=3 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 200:
        res = True
    return res


# 5.爱心使者 #


def clothes(userID: str):
    res = 0
    if bronze_clothes(userID):
        res += 1
    return res  # res为1：爱心使者（金）

# 衣物回收一次


def bronze_clothes(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=5 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) > 0:
        res = True
    return res


# 10.爱心大使 #


def clothes_lover(userID: str):
    res = 0
    if third_clothes(userID):
        res += 1
    if second_clothes(userID):
        res += 1
    if first_clothes(userID):
        res += 1
    return res  # res为1：爱心大使（铜），2:银，3:金

# 衣物回收累计10次


def third_clothes(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=5 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 10:
        res = True
    return res


# 衣物回收累计20次
def second_clothes(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=5 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 20:
        res = True
    return res

# 衣物回收累计50次


def first_clothes(userID: str):
    cursor = connection.cursor()
    cursor.execute(
        "select plogName from Plog where plogTypeID=5 and userID=%s", [userID])
    results = cursor.fetchall()
    res = False

    if len(results) >= 50:
        res = True
    return res

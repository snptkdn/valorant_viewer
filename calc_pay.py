# ランクのEnumを定義する
from enum import Enum

GM = 60

class Rank(Enum):
    IRON1 = 1
    IRON2 = 2
    IRON3 = 3
    BRONZE1 = 4
    BRONZE2 = 5
    BRONZE3 = 6
    SILVER1 = 7
    SILVER2 = 8
    SILVER3 = 9
    GOLD1 = 10
    GOLD2 = 11
    GOLD3 = 12
    DIAMOND1 = 13


# ランクごとに能力給を計算する
def calc_skill_based_pay(rank):
    if rank == Rank.IRON1:
        return 500
    elif rank == Rank.IRON2:
        return 500
    elif rank == Rank.IRON3:
        return 500
    elif rank == Rank.BRONZE1:
        return 5000
    elif rank == Rank.BRONZE2:
        return 6000
    elif rank == Rank.BRONZE3:
        return 7000
    elif rank == Rank.SILVER1:
        return 10000
    elif rank == Rank.SILVER2:
        return 12500
    elif rank == Rank.SILVER3:
        return 15000
    elif rank == Rank.GOLD1:
        return 20000
    elif rank == Rank.GOLD2:
        return 30000
    elif rank == Rank.GOLD3:
        return 40000
    elif rank == Rank.DIAMOND1:
        return 50000
    else:
        return 0

# プレイヤーごとに給与を計算する
def calc_pay(rank, pm, wm, am):
    skill_based_pay = calc_skill_based_pay(rank)
    return skill_based_pay * wm * (pm / am) ** 2 - skill_based_pay * (GM - pm)

# 受け取った数値を~万円表示にフォーマットする
def format_pay(pay):
    return str(pay // 10000) + '万円'



import random
def tao_team(players):
    random.shuffle(players)
    half = len(players) // 2
    team1 = players[:half]
    captain1 = random.choice(team1)
    team1.remove(captain1)
    team2 = players[half:]
    captain2 = random.choice(team2)
    team2.remove(captain2)
    return [(captain1, team1), (captain2, team2)]
def hien_thi_captain_of_team(teams):
    for i, (captain, team) in enumerate(teams, start = 1):
        print(f"Đội {i}: Đội trưởng - {captain}, Các thành viên - {', '.join(team)}")
def main():
    players = ["Cristiano Ronaldo", "Lionel Messi", "Erling Haaland", "Sadio Mané", "Harry Kane", "Harry Maguire", "Sergio Ramos", "N'Golo Kante"]
    while True:
        teams = tao_team(players)
        hien_thi_captain_of_team(teams)
        lua_chon = input("Bạn có muốn chọn lại đội không? (có/không): ").lower()
        if lua_chon == "không":
            print("Chương trình kết thúc.")
            break
if __name__ == "__main__":
    main()

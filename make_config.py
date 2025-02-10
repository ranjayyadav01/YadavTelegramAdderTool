import csv
import json
import re
from pathlib import Path

from init import rs, w, r, banner, clr, lg

clr()
banner()
print(f"  {r}Version: {w}3.1 {r}| Author: {w}SAIF ALI{rs}\n")
print(f"  {r}Telegram {w}@DearSaif {r}| Instagram: {w}@_Prince.Babu_{rs}\n")
print(
    f"  {r}For Get Your Group ID Add {w}@MissCutieRobot {r}To Your Group And Send /id In Your Group After Get Your Group ID Remove -100 From Your Group ID Before Enter In Script\n"
)


def check_num(phone):
    """Parses the given phone, or returns None if it's invalid."""
    if isinstance(phone, int):
        return str(phone)
    else:
        phone = re.sub(r"[+()\s-]", "", str(phone))
        if phone.isdigit():
            return phone


DEFAULT_API_ID = 29049593
DEFAULT_API_HASH = "60123a8a7984120fee1607700a713671"
DEFAULT = "UserStatus.RECENTLY"

OPTIONS = (
    "UserStatus.LAST_MONTH",
    "UserStatus.LAST_WEEK",
    "UserStatus.OFFLINE",
    "UserStatus.RECENTLY",
    "UserStatus.ONLINE",
)
config_path = Path("config.json")
delay = int(input(f" {lg}Enter Delay Timing For Per Member Adding : {w}"))
group_source = input(
    "1391787432"
)
group_target = input(
    "2365188179"
)
group_source_username = input(
    "@Rajasthan_GK_Zone"
)
if "+" in group_source_username:
    pass
else:
    group_source_username = re.sub(
        "(@)|(https://t.me/)|(http://t.me/)", "", group_source_username
    )
group_target_username = input(
    "@best_friendss_chatting"
)
if "+" in group_target_username:
    pass
else:
    group_target_username = re.sub(
        "(@)|(https://t.me/)|(http://t.me/)", "", group_target_username
    )

choice = input(
    f"\n\nType YES To Add API And HASH Manually\nType NO To Use Default One From Telegram Public API:> "
).lower()


def main():
    # for _ in range(n):
    if choice[0] == "n":
        with open("phone.csv", "r") as f:
            str_list = [row[0] for row in csv.reader(f)]
            po = 0
            if str_list:
                config = {
                    "group_source": group_source,
                    "group_target": group_target,
                    "group_source_username": group_source_username,
                    "group_target_username": group_target_username,
                    "from_date_active": DEFAULT,
                    "auto_join": True,
                    "spam_check": True,
                    "wait_time": delay,
                    "accounts": [],
                }
                for phone in str_list:
                    phone = check_num(phone)
                    po += 1
                    print(
                        f"{phone} Added To Config Run python login.py To Login Your Accounts"
                    )
                    new_account = {
                        "phone": phone,
                        "api_id": DEFAULT_API_ID,
                        "api_hash": DEFAULT_API_HASH,
                    }
                    config["accounts"].append(new_account)
            else:
                if config_path.exists():
                    with open(config_path, "r", encoding="utf-8") as file:
                        config = json.load(file)
                else:
                    config = {
                        "group_source": group_source,
                        "group_target": group_target,
                        "group_source_username": group_source_username,
                        "group_target_username": group_target_username,
                        "from_date_active": DEFAULT,
                        "auto_join": True,
                        "spam_check": True,
                        "wait_time": delay,
                        "accounts": [],
                    }
                count = int(input("How Many Numbers You Want To Add : "))
                while count > 0:
                    phon = input("Enter Your Number With Country Code : ")
                    phone = check_num(phon)
                    print(
                        f"{phone} Added To Config Path Now Run python login.py To Login Your Accounts"
                    )
                    new_account = {
                        "phone": phone,
                        "api_id": DEFAULT_API_ID,
                        "api_hash": DEFAULT_API_HASH,
                    }
                    config["accounts"].append(new_account)
                    count -= 1
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    elif choice[0] == "y":
        count = int(input("How Many Numbers You Want To Add : "))
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as file:
                config = json.load(file)
        else:
            config = {
                "group_source": group_source,
                "group_target": group_target,
                "group_source_username": group_source_username,
                "group_target_username": group_target_username,
                "from_date_active": DEFAULT,
                "auto_join": True,
                "spam_check": True,
                "wait_time": delay,
                "accounts": [],
            }
            count = int(input("How Many Numbers You Want To Add : "))
        while count > 0:
            phon = input("Enter Your Number With Country Code : ")
            phone = check_num(phon)
            apiid = int(input("Enter Your API_ID : "))
            hashid = input("Enter Your API_HASH : ")
            print(
                f"{phone} Added To Config Path Run python login.py To Login Your Accounts"
            )
            new_account = {"phone": phone, "api_id": apiid, "api_hash": hashid}
            config["accounts"].append(new_account)
            count -= 1
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    else:
        print("wrong option use YES / NO")


main()

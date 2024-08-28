import os
import random
from time import perf_counter

# v2里 - 添加了排行榜，删除了清屏

# 生成随机的3位不重复数字
def generate_secret_number():
    return ''.join(map(str, random.sample(range(10), k=3)))


def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it'
    
    clues = []
    for i, j in zip(guess, secret_number):
        if i==j:
            clues.append('Fermi')
        elif i in secret_number:
            clues.append('Pico')    
    # 提高游戏难度
    clues.sort()
    return ' '.join(clues) if clues else 'Bagels'


def is_valid_guess(guess):
    return len(guess) == 3 \
        and len(set(guess)) == len(guess) \
        and guess.isdigit()


def main():
    # 获取player姓名，初始化best score（最短用时）为正无穷大
    player_name = input('Enter your name: ')
    best_time = float('inf')

    # intro - 游戏规则
    print("I'm thinking of a 3-digit number, try to guess what it is")
    print("Here are some clues: ")
    print("Fermi - 1 digit is correct and in the right position")
    print("Pico - 1 digit is correct but in the wrong position")
    print("Bagels - none of them is correct")

    # 主游戏循环
    while 1:
        start_time = perf_counter()
        secret_number = generate_secret_number()
        attempts = 10

        while attempts>0:
            # 读入player的合法猜测
            guess = input('Enter your guess: ')
            if not is_valid_guess(guess):
                print('Invalid input, please enter a 3-digit number with unique digits')
                continue
            
            # 若猜测合法 给予相应提示
            clues = get_clues(guess, secret_number)
            print(clues)
            attempts-=1

            # 如果猜对了 - 计算用时，更新player的best score
            if guess == secret_number:
                end_time = perf_counter()
                elapsed_time = end_time - start_time
                print(f"You took {elapsed_time:.2f} seconds to guess the number")

                if best_time > elapsed_time:
                    best_time = elapsed_time
                break
            else:
                print(f"You have {attempts} attempts left")
        
        if attempts==0:
            print(f"You've run out of attempts, the number was {secret_number}")


        play_again = input("Do you want to play again? (yes or no): ")
        # player选择不继续玩时：
        if not play_again.lower().startswith('y'):
            if best_time == float('inf'):
                print("You didn't guess the number this time")
            # 1 打印player的best score（如果在游戏循环里至少猜对一次）
            else:
                print(f"Your best time was {best_time:.2f} seconds")

                # 2 读取排行榜文件到high_scores list里，添加or替换当前player的best score
                high_scores = load_high_scores()
                high_scores = update_high_scores(high_scores, best_time, player_name)

                # 3 保存并显示（前3）更新后的排行榜
                save_high_scores(high_scores)
                display_top_scores()

            break


def load_high_scores(file_path='high_scores.txt'):
    high_scores = []
    # 没有这个文件就新建 + 第一行是header 描述数据
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('time\tplayer_name\n')
    
    else:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # 检查header之外 是否有score
            if len(lines)>1:
                for line in lines[1:]:
                    try:
                        time, name = line.strip().split('\t')
                        high_scores.append((float(time), name))
                    except ValueError:
                        print('skipping invalid line')

    # 单一出口
    return high_scores


def update_high_scores(high_scores, new_best_time, player_name):
    for i, (time, name) in enumerate(high_scores):
        if name==player_name:
            if time>new_best_time:
                high_scores[i] = (new_best_time, player_name)
            break
    
    else:
        high_scores.append((new_best_time, player_name))
    
    # 在这里sort 每次update返回的都是排序后的结果
    return sorted(high_scores)


def save_high_scores(high_scores, file_path='high_scores.txt'):
    with open(file_path, 'w') as file:
        file.write('time\tplayer_name\n')
        for time, name in high_scores:
            file.write(f'{time:.2f}\t{name}\n')


def display_top_scores(file_path='high_scores.txt'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print('Top high scores: ')
        # [1:4] - 不包含header，前3名
        for rank, line in enumerate(lines[1:4], start=1):
            time, name = line.strip().split('\t')
            print(f"{rank}. {name} - {time} seconds")


if __name__ == "__main__":
    main()
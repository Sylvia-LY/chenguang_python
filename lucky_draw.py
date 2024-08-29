import random
import time

def load_participants(file_path='participants.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        # filter out empty lines
        return [line.strip() for line in file if line.strip()]

def pick_winner_v1(participants):
    return random.choice(participants)

def pick_winner_v2(participants):
    try:
        while True:
            index = int(time.time()*1000) % len(participants)
            print(f'\r{participants[index]}', end='')
            time.sleep(0.001)
    # press Ctrl + c to stop the selection process
    except KeyboardInterrupt:
        return participants[index]

def pick_winner_v3(participants):

    rand_x = random.uniform(0, 1000)
    rand_y = random.uniform(0, 1000)

    distances = []
    for participant in participants:
        id, name, x, y = participant.split('\t')
        # calculate the squared distance between 
        # the participant's coordinates and 
        # the randomly selected coordinates
        distance = (int(x)-rand_x)**2 + (int(y)-rand_y)**2
        distances.append([distance, participant])

    return min(distances, key=lambda x: x[0])[1]

def print_winner(participant):
    details = participant.split('\t')
    if len(details) == 4:
        print(f"winner: {details[1]} ID: {details[0]}")

def main():
    participants = load_participants()

    winner1 = pick_winner_v1(participants)
    winner2 = pick_winner_v2(participants)
    winner3 = pick_winner_v3(participants)
    print_winner(winner1)
    print_winner(winner2)
    print_winner(winner3)

if __name__ == "__main__":
    main()
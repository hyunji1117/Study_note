import os
import random
import time

# 화면 크기
width = 70
height = 24

# 꽃잎/반짝이 종류
petals = ["🌸", "✿", "❀", "༄", "💮"]
sparkles = ["✨", "⋆", "✦", "⋄"]

# 화면 지우기
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# 떨어지는 꽃잎 생성
blossoms = []
for _ in range(45):
    blossoms.append({
        "x": random.randint(0, width - 1),
        "y": random.randint(0, height - 1),
        "shape": random.choice(petals),
        "speed": random.choice([1, 1, 1, 2])
    })

# 반짝이 생성
twinkles = []
for _ in range(18):
    twinkles.append({
        "x": random.randint(0, width - 1),
        "y": random.randint(0, height - 1),
        "shape": random.choice(sparkles)
    })

# 바닥에 쌓이는 꽃잎
ground = ["  " for _ in range(width)]

try:
    while True:
        screen = [["  " for _ in range(width)] for _ in range(height)]

        # 반짝이 찍기
        for t in twinkles:
            if random.random() < 0.15:
                t["shape"] = random.choice(sparkles)
                t["x"] = random.randint(0, width - 1)
                t["y"] = random.randint(0, height - 4)
            screen[t["y"]][t["x"]] = t["shape"]

        # 꽃잎 찍기
        for b in blossoms:
            x, y = b["x"], b["y"]
            if 0 <= y < height and 0 <= x < width:
                screen[y][x] = b["shape"]

            # 아래로 떨어지고 좌우로 살짝 흔들림
            b["y"] += b["speed"]
            b["x"] += random.choice([-1, 0, 1])

            # 범위 보정
            b["x"] = max(0, min(width - 1, b["x"]))

            # 바닥에 닿으면 꽃잎 쌓고 다시 위에서 시작
            if b["y"] >= height - 1:
                ground[b["x"]] = random.choice(["🌸", "✿", "❀"])
                b["y"] = 0
                b["x"] = random.randint(0, width - 1)
                b["shape"] = random.choice(petals)
                b["speed"] = random.choice([1, 1, 2])

        # 바닥 꽃잎 표시
        for i in range(width):
            screen[height - 1][i] = ground[i]

        clear()
        print("🌸 벚꽃놀이 가지 말고 터미널에서 벚꽃 보자 🌸")
        print("✨ 개발자의 봄은 VSCode에서 시작됩니다... ✨\n")

        for row in screen:
            print("".join(row))

        time.sleep(0.12)

except KeyboardInterrupt:
    clear()
    print("🌸 벚꽃 애니메이션 종료! 봄날 저장 완료 🌸")
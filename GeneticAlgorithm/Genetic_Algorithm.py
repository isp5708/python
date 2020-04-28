from Genetic_Function import *

input_pw = input("비밀번호를 입력하시오 : ")
min_len = 2
max_len = 30

# 메인 부분 위는 다 함수 정의
n_generation = 100000
population = 100
best_sample = 20
lucky_few = 20
n_child = 5
chance_of_mutation = 10
x_lab = []  # x축 값
y_lab = []  # y축 값

pop = generate_population(size=population, min_len=min_len, max_len=max_len)

for g in range(n_generation):
    pop_sorted, pred_len = compute_performace(population=pop, password=input_pw)
    pop_avg = 0
    pop_sum = 0
    for i in range(len(pop_sorted)):
        pop_sum += pop_sorted[i][1]
    pop_avg = pop_sum / len(pop_sorted)

    if int(pop_sorted[0][1]) >= 100:
        x_lab.append(g + 1)  # 최종 x값 저장
        n = pop_sorted[0][1]
        y_lab.append(round(n, 2))  # 최종 y 값 100 저장 반올림 2자리 까지 출력
        print('===== %s번째 비밀번호 탐색 =====' % (g + 1))
        print(pop_sorted[0], pop_avg, sep="   ")  # 출력할 때 pop_avg sep 지우기
        print('\n비밀번호를 찾았습니다!! :  %s' % (pop_sorted[0][0]))
        print(x_lab, y_lab, sep="   ")
        break

    survivors = select_survivors(population_sorted=pop_sorted, best_sample=best_sample, lucky_few=lucky_few,
                                 password_len=pred_len)

    children = create_children(parents=survivors, n_child=n_child)

    new_generation = mutate_population(population=children, chance_of_mutation=10)

    pop = new_generation

    x_lab.append(g + 1)  # x축 저장
    y_lab.append(round(pop_avg, 2))  # y축 저장 반올림 2자리 까지 출력
    print('===== %s번째 비밀번호 탐색 =====' % (g + 1))
    print(pop_sorted[0], pop_avg, sep="   ")  # 출력할 때 pop_avg sep 지우기
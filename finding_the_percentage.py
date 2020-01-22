# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    finding_the_percentage.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashongwe <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/22 17:37:54 by ashongwe          #+#    #+#              #
#    Updated: 2020/01/22 17:37:59 by ashongwe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_list = 0
    for item in student_marks[query_name]:
         sum_list = sum_list + item
         average = sum_list/3
    print("%.2f" % average)

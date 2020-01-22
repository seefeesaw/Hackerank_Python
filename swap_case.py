# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    swap_case.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashongwe <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/22 18:21:55 by ashongwe          #+#    #+#              #
#    Updated: 2020/01/22 18:22:03 by ashongwe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def swap_case(s):
    for item in s:
        if item.isupper() == True:
            s = s.replace(item,item.lower())
        elif item.islower() == True:
            s = s.replace(item,item.upper())
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

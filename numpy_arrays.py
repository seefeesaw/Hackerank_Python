# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numpy_arrays.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ashongwe <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/08 14:36:34 by ashongwe          #+#    #+#              #
#    Updated: 2020/02/08 14:36:59 by ashongwe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr)
    i = 0
    arr = arr[::-1]
    for i,elem in enumerate(arr):
        arr[i] = numpy.char.add(elem,".")
    
    arr[0] = numpy.char.add(arr[0],".")
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

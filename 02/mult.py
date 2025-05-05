# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsaueia- <rsaueia-@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 17:12:47 by rsaueia-          #+#    #+#              #
#    Updated: 2025/05/05 17:15:19 by rsaueia-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
res = n1 * n2
if (res > 0): print("The result is positive.")
elif (res < 0): print("The result is negative.")
else: print("The result is both positive and negative.")

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsaueia- <rsaueia-@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 16:43:05 by rsaueia-          #+#    #+#              #
#    Updated: 2025/05/05 17:06:24 by rsaueia-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

n1 = int(input("Enter a number: "))
if (n1 > 0): print("This number is positive")
elif (n1 < 0): print("This number is negative")
else:
	print("This number is both positive and negative.")

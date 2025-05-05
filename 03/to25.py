# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsaueia- <rsaueia-@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/05/05 17:17:45 by rsaueia-          #+#    #+#              #
#    Updated: 2025/05/05 17:34:17 by rsaueia-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

n1 = int(input("Enter a number smaller than 25: "))
if (n1 > 25): print("Error")
while (n1 <= 25):
	print("Inside the loop, my variable is ", n1)
	n1 += 1

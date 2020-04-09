##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## make files
##

NAME	=	groundhog

SRC		=	groundhog.py

all:
	cp $(SRC) $(NAME)
	chmod 755 $(NAME)

clean:
	echo "Nothing to clean"

fclean:	clean
	rm $(NAME)	\
	rm -f *~	\
	rm -f *#	\

re:	fclean clean all

.PHONY:	all re clean fclean

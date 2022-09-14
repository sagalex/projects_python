{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba6480dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Usuário logado\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Operador ternário em Python\n",
    "\"\"\"\n",
    "logged_user = True\n",
    "msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'\n",
    "print(msg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b9a47cfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Qual a sua idade?18\n",
      "Pode acessar\n"
     ]
    }
   ],
   "source": [
    "idade = input('Qual a sua idade?')\n",
    "\n",
    "if not idade.isnumeric():\n",
    "    print('Você precisa digitar apenas números')\n",
    "else:\n",
    "    idade = int(idade)\n",
    "    e_de_maior = (idade >=18)\n",
    "    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'\n",
    "    \n",
    "    print(msg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "034dcf45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 10\n",
      "1 9\n",
      "2 8\n",
      "3 7\n",
      "4 6\n",
      "5 5\n",
      "6 4\n",
      "7 3\n",
      "8 2\n",
      "9 1\n",
      "10 0\n"
     ]
    }
   ],
   "source": [
    "for x in range(11):\n",
    "  print(x, 10-x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fa99a4c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 10\n",
      "1 9\n",
      "2 8\n",
      "3 7\n",
      "4 6\n",
      "5 5\n",
      "6 4\n",
      "7 3\n",
      "8 2\n"
     ]
    }
   ],
   "source": [
    "for i, x in enumerate(range(10, 1, -1)):\n",
    "    print(i, x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cf20f54",
   "metadata": {},
   "outputs": [],
   "source": [
    "CPF = 168.995.350-09\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c84a32f7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

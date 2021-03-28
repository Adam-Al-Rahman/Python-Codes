
import pyinputplus as pyip
import time
import colorama
# import pygame
from colorama import Fore, Back, Style

colorama.init(autoreset=True) # for not writing "\033[30m" after ever term we color
# pygame.font.init()
# font_20 = pygame.font.Font(None, 20)

print(f"{Fore.LIGHTMAGENTA_EX}POWER{Fore.RESET} of {Fore.BLUE}NUMBERS{Fore.RESET}")

print()
print("---"*20)


class PowerOfNum:

    def power_s1(self,base,exp):
        return base*self.power_s1(self,base,exp-1)

    def power_s2(self,base,exp):
        if exp==0 or base==1:
            return 1
        else:
            return base*self.power_s2(self,base,exp-1)

    def power_s3(self,base,exp):
        assert exp>=0 and int(exp)==exp,'Exponent should be positive & integer'
        if exp==0 or base==1:
            return 1
        else:
            return base * self.power_s3(self,base,exp - 1)

class CHOOSE:
    base_input = pyip.inputNum(f"{Fore.LIGHTRED_EX}Base{Fore.RESET}: ")
    exp_input = pyip.inputNum(f"{Fore.LIGHTRED_EX}Exponent{Fore.RESET}: ",min=0)
    choose = input("STEPS - [ power_s1,power_s2,power_s3 ] : ")

    def __init__(self):
        if self.choose.casefold() == "power_s1":
            print()
            print(f"{Fore.LIGHTMAGENTA_EX}[*] Note - You will get an error here, because of infinte recursion"
                  "RecursionError: maximum recursion depth exceeded")
            time.sleep(2)
            print()
            print(PowerOfNum.power_s1(PowerOfNum,self.base_input,self.exp_input))
            print("hwll")
        elif self.choose.casefold() == "power_s2":
            print(PowerOfNum.power_s2(PowerOfNum,self.base_input,self.exp_input))

        elif self.choose.casefold() == "power_s3":
            print(PowerOfNum.power_s3(PowerOfNum,self.base_input,self.exp_input))
        else:
            print(f"{Fore.BLUE}choose one of in (power_s1,power_s2,power_s3)")

while True:
    CHOOSE()
    class Repeat(CHOOSE):
        choose = input(f"Wanna try different step or difval for [{Fore.LIGHTMAGENTA_EX}Base, Exponent{Fore.RESET}] "
                       f"other than {Fore.LIGHTMAGENTA_EX}[{CHOOSE().choose}]{Fore.RESET} in"
                       f" (power_s1,power_s2,power_s3 , {Fore.RED}difval, quit{Fore.RESET}): ")
        def __init__(self):
            super().__init__()
            if self.choose.casefold() == "quit":
                print(f"{Fore.LIGHTYELLOW_EX}See Yaah 👋🏻{Fore.RESET}")
                exit()
    Repeat()

    # class DifferentVal(Repeat):
    #     def difvalue(self):
    #         if Repeat().choose.casefold()=="difval":
    #             base_input = pyip.inputNum(f"{Fore.LIGHTRED_EX}Base{Fore.RESET}: ")
    #             exp_input = pyip.inputNum(f"{Fore.LIGHTRED_EX}Exponent{Fore.RESET}: ",min=0)
    #             Repeat()
    #
    # DifferentVal()








##Faça um Programa que peça os 3 lados de um triângulo.
## O programa deverá informar se os valores podem ser um triângulo.
## Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.Dicas:Três lados formam um triângulo quando
## a soma de quaisquer dois lados for maior que o terceiro;Triângulo Equilátero: três lados iguais;Triângulo Isósceles: quaisquer dois lados iguais;
##Triângulo Escaleno: três lados diferentes;

print("------------------------------------------------")
l1 = int(input("Digite o comprimento do primeiro lado do triangulo."))
l2 = int(input("Digite o comprimento do segundo lado do triangulo."))
l3 = int(input("Digite o comprimento do terceiro lado do triangulo."))
print(" VERIFICANDO SE PODE SER UM TRIANGULO... ")

if(l1 + l2> l3 or l1+l3> l2 or l2+l3> l1):
        print(" As medidas informadas formam um triangulo!")
        if(l1==l2==l3):
            print("O triangulo informado é Equilátero.")
        else:
            if(l1==l2 or l2==l3 or l3==l1):
                print("O triangulo informado é Isosceles.")
            else:
                print("O triangulo informado é Escaleno.")
else:
        print("As medidas informados nao formam um triangulo.")

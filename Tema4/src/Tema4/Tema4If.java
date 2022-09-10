package Tema4;

import java.util.Scanner;

public class Tema4If {
    public static void main(String[] args) {
    numif();
    }
    public static void numif() {
        Scanner sc = new Scanner(System.in);
        int numeroIf;
        System.out.println("Introduce un numero");
        numeroIf = sc.nextInt();
            if (numeroIf > 0) {
                System.out.println("El numero es positivo");
            }
            else if (numeroIf < 0) {
                System.out.println("El numero es negativo");
            }
            else {
                System.out.println("El numero es 0");
            }
        }
}
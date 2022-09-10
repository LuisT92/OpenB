package Tema4;

import java.util.Scanner;

public class Tema4Switch {
    public static void main(String[] args) {
        estacion();
    }

    public static void estacion(){
        Scanner sc = new Scanner(System.in);
        int estacion;
        System.out.println("Introduce un numero del 1 al 4 para saber la estacion del año a la que pertenece");
        estacion = sc.nextInt();
        switch (estacion) {
            case 1:
                System.out.println("Primavera");
                break;
            case 2:
                System.out.println("Verano");
                break;
            case 3:
                System.out.println("Otoño");
                break;
            case 4:
                System.out.println("Invierno");
                break;
            default:
                System.out.println("Oye, solo hay 4 estaciones");
                break;
        }
    }
}

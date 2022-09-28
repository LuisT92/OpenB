package Tema9;

public class main {
    public static void main (String []args) {
        Cliente banco = new Cliente();

        banco.setNombre("Luis");
        banco.setEdad(30);
        banco.setTelefono("5523415623");
        banco.setCredito(90000);

        System.out.println("Nombre: "+ banco.getNombre());
        System.out.println("Edad: "+ banco.getEdad());
        System.out.println("Telefono: "+ banco.getTelefono());
        System.out.println("Linea de credito: " + banco.getCredito());

        Trabajador basico = new Trabajador();

        basico.setNombre("Luis Torres");
        basico.setEdad(30);
        basico.setTelefono("5523415623");
        basico.setSalario(26000);

        System.out.println("Nombre: "+ basico.getNombre());
        System.out.println("Edad: "+ basico.getEdad());
        System.out.println("Telefono: "+ basico.getTelefono());
        System.out.println("Linea de credito: " + basico.getSalario());
    }

}

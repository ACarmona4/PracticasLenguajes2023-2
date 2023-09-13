class Main{

    public static void run(){

        //Crear las instancias de las diferentes clases
        Administrador admin1 = new Administrador("Juan", "juan55@xyz.com", 4321);
        Cajero cajero1 = new Cajero("Raul", "raul05@xyz.com", 1234);
        Cliente cliente1 = new Cliente("Camilo", "camilo@gmail.com", "3001234567", "Calle 123 # 45 - 67");
        Cliente cliente2 = new Cliente("Tomas", "tomasg@hotmail.com", "3249876341", "Carrera 16a #15 - 20");

        //Mostrar el contenido de cada una de los objetos creados
        System.out.println(" ");
        System.out.println("ADMINISTRADOR ------------------");
        admin1.mostrarContenido();
        admin1.asignarCodigoPerfil(4321, cajero1);
        admin1.asignarCodigoPerfil(4321, cliente1);
        admin1.asignarCodigoPerfil(4321, cliente2);
        System.out.println(" ");

        System.out.println("CAJERO ------------------");
        cajero1.mostrarContenido();
        cajero1.registrarVenta(1234);
        System.out.println(" ");

        System.out.println("CLIENTE 1 ------------------");
        cliente1.mostrarContenido();
        cliente1.consultarProductos();
        System.out.println(" ");

        System.out.println("CLIENTE 2 ------------------");
        cliente2.mostrarContenido();
        cliente2.consultarProductos("x");
        System.out.println(" ");

    }

    public static void main(String[] args) {
        run();
    }

}
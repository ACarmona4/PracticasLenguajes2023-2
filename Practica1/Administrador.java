public class Administrador {

    private String nombre;
    private String correo;
    private int claveAdministrador;
    private String codigoPerfil;

    public Administrador(String nombre, String correo, int claveAdministrador) {
        this.nombre = nombre;
        this.correo = correo;
        this.claveAdministrador = claveAdministrador;
        this.codigoPerfil = "001";
    }

    //Métodos para asignar el código a un perfil
    public void asignarCodigoPerfil(int claveAdministrador, Cajero cajero){
        if (claveAdministrador == this.claveAdministrador){
        cajero.setCodigoPerfil("002");
        System.out.println("El administrador " + this.nombre + " le ha asignado exitosamente el código al perfil del cajero " + cajero.getNombre());
        }else{
            System.out.println("ERROR! Clave ingresada incorrecta, no se ha asignado el código al perfil del cajero " + cajero.getNombre() +". Intente nuevamente.");
        }
    }

    public void asignarCodigoPerfil(int claveAdministrador, Cliente cliente){
        if (claveAdministrador == this.claveAdministrador){
        cliente.setCodigoPerfil("003");
        System.out.println("El administrador " + this.nombre + " le ha asignado exitosamente el código al perfil del cliente " + cliente.getNombre());
        }else{
            System.out.println("ERROR! Clave ingresada incorrecta, no se ha asignado el código al perfil del cliente " + cliente.getNombre() +". Intente nuevamente.");
        }
    }

    //Método para mostrar el contenido del objeto
    public void mostrarContenido(){
        System.out.println("Nombre: " + this.nombre + " - Correo: " + this.correo + " - Clave Administrador: " + this.claveAdministrador + ".Este usuario es un administrador, puede: asignar códigos a un perfil. El código de este perfil es: " + this.codigoPerfil);
    }

    //Setters y getters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public int getClaveAdministrador() {
        return claveAdministrador;
    }

    public void setClaveAdministrador(int claveAdministrador) {
        this.claveAdministrador = claveAdministrador;
    }

    public String getCodigoPerfil() {
        return codigoPerfil;
    }

    public void setCodigoPerfil(String codigoPerfil) {
        this.codigoPerfil = codigoPerfil;
    }
    
}

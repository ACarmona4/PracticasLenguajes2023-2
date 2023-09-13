public class Cajero {
    
    private String nombre;
    private String correo;
    private int claveCajero;
    private String codigoPerfil;

    public Cajero(String nombre, String correo, int claveCajero) {
        this.nombre = nombre;
        this.correo = correo;
        this.claveCajero = claveCajero;
        this.codigoPerfil = "No asignado";
       
    }

    //Método para registrar una venta
    public void registrarVenta(int claveCajero) {
        
        if (claveCajero == this.claveCajero){
            System.out.println("Clave correcta! El cajero " + this.nombre + " ha registrado la venta de un producto");
        }else{
            System.out.println("ERROR! Clave incorrecta, no se ha registrado la venta. Intente nuevamente.");
        }
    }
    
    //Método para mostrar el contenido del objeto
    public void mostrarContenido(){
        System.out.println("Nombre: " + this.nombre + " - Correo: " + this.correo + " - Clave Cajero: " + this.claveCajero + ". Este usuario es un cajero, puede: registar ventas. El código de este perifl es: " + this.codigoPerfil);
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

    public int getClaveCajero() {
        return claveCajero;
    }

    public void setClaveCajero(int claveCajero) {
        this.claveCajero = claveCajero;
    }

    public String getCodigoPerfil() {
        return codigoPerfil;
    }

    public void setCodigoPerfil(String codigoPerfil) {
        this.codigoPerfil = codigoPerfil;
    }
    
}

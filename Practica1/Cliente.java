class Cliente {
    
    private String nombre;
    private String correo;
    private String telefono;
    private String direccion;
    private String codigoPerfil;

    public Cliente(String nombre, String correo, String telefono, String direccion) {
        this.nombre = nombre;
        this.correo = correo;
        this.telefono = telefono;
        this.direccion = direccion;
        this.codigoPerfil = "No asignado";
    }

    //Métodos para consultar productos
    public void consultarProductos (String filtro) {
        System.out.println("Has accedido a ver solo las prendas superiores: ");
        System.out.println("Camisas = 100.000 " + "\n" + "Gafas = 250.000 " + "\n" + "Buzo = 300.000 " );
    }
    public void consultarProductos () {
        System.out.println("Has accedido a ver todas las prendas: ");
        System.out.println("Camisas = 100.000 " + "\n" + "Gafas = 250.000 " + "\n" + "Buzo = 300.000 " 
        + "Gafas = 250.000 " + "\n" + "Pantalones = 250.000" + '\n' + "Jean = 300.000" + "\n" + "Tenis = 500.000");
    }

    //Método para mostrar el contenido del objeto
    public void mostrarContenido(){
        System.out.println("Nombre: " + this.nombre + " - Correo: " + this.correo + " - Telefono de contacto: " + this.telefono
        + " - Dirección: " + this.direccion + " - Este usuario es un cliente, puede: consultar productos. El código de este perfil es: " + this.codigoPerfil);
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

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getCodigoPerfil() {
        return codigoPerfil;
    }

    public void setCodigoPerfil(String codigoPerfil) {
        this.codigoPerfil = codigoPerfil;
    }

    
}

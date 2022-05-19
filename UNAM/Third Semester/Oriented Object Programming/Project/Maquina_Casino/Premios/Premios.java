package Premios;

public interface Premios {
    /** Obtener los posibles premios */
    public int getTres();
    public int getCuatro();
    public int getCinco();

    /** Obtener y modificar el nombre */
    public String getName();
    public String getNomString();
    public void setNomString(String name);

    /** Agregar metodo que guarde y regrese color */
    public String getColor();
    public void setColor(String color);

    /** Patron de diseño Prototype */
    public Premios clone();
}
package Premios;

public class Uvas implements Premios {

    private int cincoUvas = 650;
    private int cuatroUvas = 325;
    private int tresUvas = 160;
    private String name = "Uva";
    private String color = "\033[37m";

    /** Obtiene y asigna el nombre */
    public String getName() {
        return "    "+name+"   ";
    }
    public String getNomString(){
        return name;
    }
    public void setNomString(String name){
        this.name = name;
    }

    /** Obtiene los 3 posibles premios */
    public int getCinco(){
        return cincoUvas;
    }
    public int getCuatro(){
        return cuatroUvas;
    }
    public int getTres(){
        return tresUvas;
    }

    /** Agregar metodo que guarde y regrese color */
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }

    /** Patron de diseño Prototype */
    public Premios clone() {
        return new Uvas();
    }
}
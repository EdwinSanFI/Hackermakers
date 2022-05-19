package Premios;
import java.util.Random;

public class TirarPalanca {
    public int Jugar(){
        final String RESET = "\u001B[0m";
        Cereza cereza = new Cereza();
        Comodin comodin = new Comodin();
        Diamantes diamantes = new Diamantes();
        Sandia sandia = new Sandia();
        Sietes sietes = new Sietes();
        Treboles treboles = new Treboles();
        Uvas uvas = new Uvas();
        Random random = new Random();
        int creditos;

        /** Atributo del usuario */
        int puntuacion = 0;
        Premios[][] ruleta = new Premios[3][5];

        /** Asigna valores aleatorios */
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                int valor = random.nextInt(0, 101);
                /** 5% */
                if (valor >= 0 && valor <= 5) {
                    ruleta[i][j] = comodin.clone();
                /** 10% */
                } else if (valor > 5 && valor <= 15) {
                    ruleta[i][j] = sietes.clone();
                /** 15% */
                } else if (valor > 15 && valor <= 25) {
                    ruleta[i][j] = diamantes.clone();
                /** 15% */
                } else if (valor > 25 && valor <= 45) {
                    ruleta[i][j] = treboles.clone();
                /** 15% */
                } else if (valor > 45 && valor <= 60) {
                    ruleta[i][j] = cereza.clone();
                /** 20% */
                } else if (valor > 60 && valor <= 80) {
                    ruleta[i][j] = sandia.clone();
                /** 20% */
                } else if (valor > 80 && valor <= 100) {
                    ruleta[i][j] = uvas.clone();
                }
            }
        }


        /** Pruebas */

        // ruleta[0][0] = comodin.clone();
        // ruleta[1][1] = comodin.clone();
        // ruleta[2][2] = comodin.clone();
        // ruleta[1][3] = comodin.clone();
        // ruleta[0][4] = comodin.clone();


        creditos = revisarLinea(puntuacion, ruleta);

        imprimirRuleta(ruleta, RESET);
        /** Lo puse despues para que al imprimir aparezcan aquellos espacios ganadores */
        return creditos;
    }

    /** Imprime la ruleta */
    public void imprimirRuleta(Premios ruleta[][], String reset){
        /** Imprimir la info de la ruleta */
        for (int i = 0; i < 3; i++) {
            System.out.print(" | ");
            for (int j = 0; j < 5; j++) {
                if(ruleta[i][j].getNomString() == ruleta[i][j].getNomString().toUpperCase()) {
                    System.out.print(ruleta[i][j].getColor() + ruleta[i][j].getName() + reset+ " | ");
                }else {
                    System.out.print(ruleta[i][j].getColor() + ruleta[i][j].getName() + reset +" | ");
                }
            }
            System.out.println();
        }

    }

    /** Revisa que linea de premio hay */
    public int revisarLinea(int puntuacion, Premios ruleta[][]){
        /** Tres primeras lineas de premios */
        for(int i = 0; i < 3; i++){
            if(ruleta[i][0].getNomString().equals(ruleta[i][1].getNomString()) && ruleta[i][0].getNomString().equals(ruleta[i][2].getNomString())){
                if (ruleta[i][2].getNomString().equals(ruleta[i][3].getNomString())){
                    if(ruleta[i][3].getNomString().equals(ruleta[i][4].getNomString())){
                        ruleta[i][0].setColor("\033[31m");
                        ruleta[i][1].setColor("\033[31m");
                        ruleta[i][2].setColor("\033[31m");
                        ruleta[i][3].setColor("\033[31m");
                        ruleta[i][4].setColor("\033[31m");
                        puntuacion += ruleta[i][4].getCinco();
                        continue;
                    } else{
                        ruleta[i][0].setColor("\033[36m");
                        ruleta[i][1].setColor("\033[36m");
                        ruleta[i][2].setColor("\033[36m");
                        ruleta[i][3].setColor("\033[36m");
                        puntuacion += ruleta[i][3].getCuatro();
                        continue;
                    }
                } else {
                    puntuacion += ruleta[i][0].getTres();
                }
                ruleta[i][0].setColor("\033[33m");
                ruleta[i][1].setColor("\033[33m");
                ruleta[i][2].setColor("\033[33m");
            }
        }

        /** Cuarta linea de premios V */
        if (ruleta[2][0].getNomString().equals(ruleta[1][1].getNomString()) && ruleta[1][1].getNomString().equals(ruleta[0][2].getNomString()) ) {
            if(ruleta[0][2].getNomString().equals(ruleta[1][3].getNomString())) {
                if(ruleta[1][3].getNomString().equals(ruleta[2][4].getNomString())) {
                    ruleta[2][0].setColor("\033[32m");
                    ruleta[1][1].setColor("\033[32m");
                    ruleta[0][2].setColor("\033[32m");
                    ruleta[1][3].setColor("\033[32m");
                    ruleta[2][4].setColor("\033[32m");
                    puntuacion += ruleta[2][4].getCinco();
                } else {
                    ruleta[2][0].setColor("\033[32m");
                    ruleta[1][1].setColor("\033[32m");
                    ruleta[0][2].setColor("\033[32m");
                    ruleta[1][3].setColor("\033[32m");
                    puntuacion += ruleta[1][3].getCuatro();
                }
            } else {
                ruleta[2][0].setColor("\033[32m");
                ruleta[1][1].setColor("\033[32m");
                ruleta[0][2].setColor("\033[32m");
                puntuacion += ruleta[0][2].getTres();
            }
        }

        /** Quinta linea de premios /\ */
        if (ruleta[0][0].getNomString().equals(ruleta[1][1].getNomString()) && ruleta[1][1].getNomString().equals(ruleta[2][2].getNomString()) ) {
            if(ruleta[2][2].getNomString().equals(ruleta[1][3].getNomString())){
                if(ruleta[1][3].getNomString().equals(ruleta[0][4].getNomString())){
                    ruleta[0][4].setColor("\033[35m");
                    ruleta[0][0].setColor("\033[35m");
                    ruleta[1][1].setColor("\033[35m");
                    ruleta[2][2].setColor("\033[35m");
                    ruleta[1][3].setColor("\033[35m");
                    puntuacion += ruleta[0][4].getCinco();
                } else {
                    ruleta[0][0].setColor("\033[35m");
                    ruleta[1][1].setColor("\033[35m");
                    ruleta[2][2].setColor("\033[35m");
                    ruleta[1][3].setColor("\033[35m");
                    puntuacion += ruleta[1][3].getCuatro();
                }
            } else {
                ruleta[0][0].setColor("\033[35m");
                ruleta[1][1].setColor("\033[35m");
                ruleta[2][2].setColor("\033[35m");
                puntuacion += ruleta[2][2].getTres();
            }
        }

        /** Retorna la puntuacion */
        if(puntuacion == 0){
            System.out.println("\nGanaste: " + "0" + " " + "Puntos");
        } else {
            System.out.println("\nGanaste: " + puntuacion + " " + "Puntos");
        }

        return puntuacion;
    }
}

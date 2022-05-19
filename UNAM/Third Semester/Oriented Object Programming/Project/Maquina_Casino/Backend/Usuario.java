package Backend;
import java.util.*;
import java.io.*;
import Premios.*;

public class Usuario{

    static String usuario;
    static String contrasena;
    static float pesos = 0;
    static float creditos = 0;
    static int success = 0;
    String datosUsuario = "";
    TirarPalanca tp = new TirarPalanca();

    public void escribir(String datos) {
        // Writing in the file the data of the user when he/she creates an account
        try {
            try {
                BufferedWriter bw = new BufferedWriter(new FileWriter("cuentas.csv",true));
                bw.write(datos);
                bw.close();
            } catch (FileNotFoundException e) {
                e.getMessage();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void crearCuenta() {
        // Variables for the passwords
        char [] contr1;
        char [] contr2;

        // Creating the account of the user
        System.out.println("\nCREAR CUENTA\n");
        Console c = System.console();

        // Obtaining the name of the user
        System.out.println("Ingresar Usuario: ");
        usuario = c.readLine();

        // Obtaining the password of the user

        /** Poner ciclo while aqui para que contra 1 y 2 cuando no sean iguales se repita el codigo */
        System.out.println("Ingresar contrasena: ");
        contr1 = c.readPassword();
        System.out.print("Ingresa contrasena de nuevo: ");
        contr2 = c.readPassword();

        if(!Arrays.equals(contr1, contr2)) {
            while(!Arrays.equals(contr1, contr2)) {
                System.out.println("\n\tLas contrasenas no coinciden, intente de nuevo\n");
                System.out.println("Ingresar contrasena: ");
                contr1 = c.readPassword();
                System.out.print("Ingresa contrasena de nuevo: ");
                contr2 = c.readPassword();
            }
        }

        System.out.println("\nCuenta creada con exito!");

        // Concatenating the user's name, user's password, user's money and user's credtis to the end of the user's data.
        datosUsuario += usuario + ",";
        datosUsuario += new String(contr1) + ",";
        datosUsuario += "0.00,";
        datosUsuario += "0.00\n";

        // Writing the user's data in the file
        escribir(datosUsuario);

        // Clean the string.
        datosUsuario = "";
    }

    public String[] iniciarSesion() {
        Console cis = System.console();
        System.out.println("\n\t\tINICIAR SESION\n");

        // Asking the user to input a username.
        System.out.println("Usuario: ");
        String us_is = cis.readLine();

        // Reading the password from the console.
        System.out.println("Contrasena: ");
        char [] con_is = cis.readPassword();
        String con_string = String.valueOf(con_is);

        // Reading a csv file and checking if the username and password are correct.
        try {
            try {
                BufferedReader csvReader = new BufferedReader(new FileReader("cuentas.csv"));
                String line = csvReader.readLine();
                while (line != null && success != 1) {
                    String[] info = line.split(",");
                    if (us_is.equals(info[0]) && con_string.equals(info[1])) {
                        System.out.println("Inicio de sesion correcto");
                        success = 1;
                        return info;
                    }
                    line = csvReader.readLine();
                }
                if (Usuario.success != 1) {
                    Usuario.success = 0;
                    System.out.println("Inicio de sesion incorrecto");
                }
                csvReader.close();
            } catch (FileNotFoundException e) {
                e.getMessage();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void bienvenida(String[] usuario){
        /** Nombre del usuario */
        System.out.println("\nBienvenido, "+usuario[0]);
        /** Saldo del usuario */
        System.out.println("Saldo disponible: "+usuario[2]);
        /** Creditos del usuario */
        System.out.println("Creditos disponibles: "+usuario[3]);
    }

    public void ingresarPesos(float ingresapesos) {
        Usuario.pesos += ingresapesos;
        System.out.println("El nuevo saldo es: " + Usuario.pesos);
        // Usuario.datosInternos.set(2, Float.toString(Usuario.pesos));
    }

    public void pesosACreditos(float pesacred) {
        if (Usuario.pesos != 0 && Usuario.pesos >= pesacred) {
            Usuario.creditos += pesacred*10;
            System.out.println("La nueva cantidad de creditos es: " + Usuario.creditos);
            System.out.println("Pesos restantes: "+Usuario.pesos);
            Usuario.pesos -= pesacred;
            // Usuario.datosInternos.set(2, Float.toString(Usuario.pesos));
            // Usuario.datosInternos.set(3, Float.toString(Usuario.creditos)); 
        } else {
            System.out.println("No hay pesos suficientes");
        }
    }

    public void creditosAPesos(float credapes) {
        if (Usuario.creditos != 0 && Usuario.creditos >= credapes) {
            Usuario.pesos += credapes*0.1;
            System.out.println("La nueva cantidad de pesos es: " + Usuario.pesos);
            Usuario.creditos -= credapes;
            // Usuario.datosInternos.set(3, Float.toString(Usuario.creditos));
            // Usuario.datosInternos.set(2, Float.toString(Usuario.pesos));
        } else {
            System.out.println("No hay creditos suficientes");
        }
    }

    public void retirarPesos (float retpes) {
    	if (Usuario.pesos != 0 && Usuario.pesos >= retpes) {
    		Usuario.pesos -= retpes;
	    	System.out.println(retpes+" pesos retirados. "+ Usuario.pesos+" restantes");
            // Usuario.datosInternos.set(2, Float.toString(Usuario.pesos));
	    } else {
	     System.out.println("No hay dinero suficiente");
	    }
    }

    public void listaPremios () {

        ArrayList<String[]> premios = new ArrayList<>();
        String[] cabecera = {"Nombre", "3 objetos", "4 objetos", "5 objetos"};
        premios.add(cabecera);

        Premios uvas = new Uvas();
    	String [] premiosUvas = {"Uva",Integer.toString(uvas.getTres()), Integer.toString(uvas.getCuatro()), Integer.toString(uvas.getCinco())};
        premios.add(premiosUvas);

        Premios cerezas = new Cereza();
    	String [] premiosCereza = {"Cereza",Integer.toString(cerezas.getTres()), Integer.toString(cerezas.getCuatro()), Integer.toString(cerezas.getCinco())};
        premios.add(premiosCereza);

        Premios comodin = new Comodin();
    	String [] premiosComodin = {"Comodin",Integer.toString(comodin.getTres()), Integer.toString(comodin.getCuatro()), Integer.toString(comodin.getCinco())};
        premios.add(premiosComodin);

        Premios diamante = new Diamantes();
    	String [] premiosDiamante = {"Diamante",Integer.toString(diamante.getTres()), Integer.toString(diamante.getCuatro()), Integer.toString(diamante.getCinco())};
        premios.add(premiosDiamante);

        Premios sandia = new Sandia();
    	String [] premiosSandia = {"Sandia",Integer.toString(sandia.getTres()), Integer.toString(sandia.getCuatro()), Integer.toString(sandia.getCinco())};
        premios.add(premiosSandia);

        Premios siete = new Sietes();
    	String [] premiosSiete = {"Siete",Integer.toString(siete.getTres()), Integer.toString(siete.getCuatro()), Integer.toString(siete.getCinco())};
        premios.add(premiosSiete);

        Premios trebol = new Treboles();
    	String [] premiosTrebol = {"Trebol",Integer.toString(trebol.getTres()), Integer.toString(trebol.getCuatro()), Integer.toString(trebol.getCinco())};
        premios.add(premiosTrebol);

        for (String[] premio : premios) {
    		System.out.println(premio[0]+": "+premio[1]+" "+premio[2]+" "+premio[3]);
    	}
    }

    // Este es un metodo que cree para modificar los creditos del usuario una vez que gana
    public void modificarCreditos(int creditos, String[] usuario) {
        try {
            BufferedReader csvReader = new BufferedReader(new FileReader("cuentas.csv"));
            String line = csvReader.readLine();
            // Como es una linea de STRING con ",", se separa para que se obtenga en [] y acceder mas facil
            String[] info = line.split(",");
            // Cuando se obtenga la linea del usuario a modificar
            while (!info[0].equals(usuario[0]) ) {
                line = csvReader.readLine();
                info = line.split(",");
            }
            System.out.println("Viejo: "+line.split(",")[3]);
            line.split(",")[3] = Integer.toString(Integer.parseInt(line.split(",")[3])+ creditos);
            System.out.println("Nuevo:"+Integer.toString(Integer.parseInt(line.split(",")[3])+ creditos));
            // YA, PERO FALTA MODIFCAR AL ARCHIVOO PTM
            // csvReader.;
            csvReader.close();
        } catch (FileNotFoundException e) {
            e.getMessage();
        } catch (IOException e) {
            e.getMessage();
        }
    }

    // Metodo main
    public void main() {
        // Console s = System.console();
        Scanner sc = new Scanner(System.in);
        int opc = 0;
        int opcInicio = 0;
        int opc2 = 0;
        String usuario[] = null;
        int creditosGanados;
        String menu = "\n1. Jugar" +
                "\n2. Modificar cuenta" +
                "\n3. Ver lista de premios" +
                "\n4. Salir";

        String menuInicio = "\n1. Crear cuenta"+
                            "\n2. Iniciar sesion";

        String menuModificar = "\n\t1. Ingresar pesos" +
                                "\n\t2. Pesos a creditos" +
                                "\n\t3. Creditos a pesos" +
                                "\n\t4. Retirar pesos" +
                                "\n\t5. Guardar y salir";

        System.out.println("\nElige una opcion: "+menuInicio);
        opcInicio = sc.nextInt();

        while (opcInicio > 0 && opcInicio < 3) {
            switch (opcInicio) {
                case 1:
                /** Se crea la cuenta y se guarda en cuentas.csv con exito */
                    crearCuenta();
                    System.out.println(menuInicio);
                    opcInicio = sc.nextInt();
                    break;
                case 2:
                /** Cuando ingrese el usuario, se guarda su info en un String[] */
                    usuario = iniciarSesion();
                    opcInicio = 3;
            }
        }

        /** 2 */
        if (usuario != null) {
            // Guarda los creditos del usuario
            int creditosGuardados = Integer.parseInt(usuario[3]);

            // Metodo de bienvenida al usuario
            bienvenida(usuario);

            System.out.println("\nElige opcion: " + menu);
            opc = sc.nextInt();
            while (opc > 0 && opc < 4) {
                switch (opc) {
                    case 1:
                    // Mientras que los creditos del usuario no sean 0
                        if (creditosGuardados != 0) {
                            creditosGanados = tp.Jugar();
                            if (creditosGanados > 0) {
                                // Se puede jugar y este retorna los creditos ganados
                                creditosGuardados += creditosGanados;
                                // Metodo para sobreescribir los creditos en el archivo
                                modificarCreditos(creditosGuardados, usuario);
                            } else {
                                System.out.println("No ganaste nada, suerte para la proxima");
                            }
                        } else {
                            System.out.println("\nAgrega creditos primero");
                        }
                        break;
                    case 2:
                        System.out.println("\tMODIFICAR CUENTA");
                        System.out.println("\tElige una opcion: " + menuModificar);
                        opc2 = sc.nextInt();
                        do {
                            switch (opc2) {
                                case 1:
                                    System.out.println("\t\tINGRESAR PESOS");
                                    System.out.println("\tCantidad de pesos a ingresar: ");
                                    float ingresapesos = sc.nextFloat();
                                    ingresarPesos(ingresapesos);
                                    System.out.println(menuModificar);
                                    opc2 = sc.nextInt();
                                    sc.nextLine();
                                    break;
                                case 2:
                                    System.out.println("\t\tPESOS A CREDITOS");
                                    System.out.println("\tPesos disponibles: " + Usuario.pesos);
                                    System.out.println("\tCantidad de pesos que desea convertir a creditos: ");
                                    float pesacred = sc.nextFloat();
                                    pesosACreditos(pesacred);
                                    System.out.println(menuModificar);
                                    opc2 = sc.nextInt();
                                    sc.nextLine();
                                    break;
                                case 3:
                                    System.out.println("\t\tCREDITOS A PESOS");
                                    System.out.println("\tCreditos disponibles: " + creditos);
                                    System.out.println("\tCantidad de creditos que desea convertir a pesos: ");
                                    float credapes = sc.nextFloat();
                                    creditosAPesos(credapes);
                                    System.out.println(menuModificar);
                                    opc2 = sc.nextInt();
                                    sc.nextLine();
                                    break;
                                case 4:
                                    System.out.println("\t\tRETIRAR PESOS");
                                    System.out.println("\tPesos disponibles: " + Usuario.pesos);
                                    System.out.println("\tCuanto desea retirar? ");
                                    float retpes = sc.nextFloat();
                                    retirarPesos(retpes);
                                    System.out.println(menuModificar);
                                    opc2 = sc.nextInt();
                                    sc.nextLine();
                                    break;
                                case 5:
                                    // Usuario.escribir(datos);
                                    System.out.println("\nVolviendo...");
                                    System.out.println("Elige opcion: " + menu);
                                    opc2 = 6;
                                    opc = sc.nextInt();
                                    break;
                                default:
                                    System.out.println("\tElige una opcion correcta" + menuModificar);
                                    opc2 = sc.nextInt();
                                    break;
                            }
                        } while (opc2 > 0 && opc2 < 6);

                        break;
                    case 3:
                        listaPremios();
                        System.out.println(menu);
                        opc = sc.nextInt();
                        sc.nextLine();
                        break;
                    case 4:
                        System.out.println("Gracias por jugar con nostros!!");
                        opc += opc;
                        break;
                    default:
                        System.out.println("Escoge una opcion correcta");
                        System.out.println(menu);
                        opc = sc.nextInt();
                        sc.nextLine();
                        break;
                }
                System.out.println("\nElige opcion: " + menu);
                opc = sc.nextInt();
            }
        } else {
            Usuario.success = 0;
            System.out.println("Suerte para la proxima");
        }
    }

    



    /** Mejora en un futuro */
    // public String[] buscarUsuario(String nombreUsuario) {
    //     try {
    //         BufferedReader csvReader = new BufferedReader(new FileReader("cuentas.csv"));
    //         String line = csvReader.readLine();
    //         String[] info = line.split(",");
    //         while (line.split(",")[0] != null || line.split(",")[0] != nombreUsuario) {
    //             if (nombreUsuario == info[0]) {
    //                 return info;
    //             }
    //             line = csvReader.readLine();
    //         }
    //         csvReader.close();
    //     } catch (FileNotFoundException e) {
    //         e.getMessage();
    //     } catch (IOException e) {
    //         e.getMessage();
    //     }
    //     return null;
    // }

}

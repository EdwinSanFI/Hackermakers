public class StringReverse{

    public String reverseString(String str){
        if(str.isEmpty()){
            return str;
        } else {
            return reverseString(str.substring(1))+str.charAt(0);
        }
    }
    public static void main(String[] args){
        StringReverse obj = new StringReverse();
        String result = obj.reverseString("Algorithms are love");
        System.out.println(result);
    }
    }

    //Esto hace que la palabra "Algorithms are love, se imprima en pantalla al revés, de la últimia letra de la oración a la primera."
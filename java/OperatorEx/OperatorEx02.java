package OperatorEx;
 
// 산술 연산자 연습 +, - , *, /, %
// 부정 연산자 연습 !
 
import javax.swing.JOptionPane;
 
public class OperatorEx02 {
 
    public static void main(String[] args) {
 
        int share = 10 / 8;   //몫
        int remain = 10 % 8;  //나머지
        int remn = 10 - (share * 8);  //나머지
        
        System.out.println("몫은 " + share + " 이고 : 너머지는 " + remain);
        
        int aaa = 2 - -3;
        System.out.println(aaa);
        
        int a_aa = -3;
        int a_bb = 5 - -a_aa;
        System.out.println(a_bb);
        
        
        //문제 
        // JOptionPane 을 이용하여  숫자 두개  int aa;  숫자 int bb; 입력받고,
        // + , -, *, / 결과 출력  예제를 만들어 보자~~
        
//        int aa = Integer.parseInt(JOptionPane.showInputDialog("첫번째 숫자를 입력해 주세요"));
//        int bb = Integer.parseInt(JOptionPane.showInputDialog("두번째 숫자를 입력해 주세요"));        
//        System.out.println(aa + " + " + bb + " = " + (aa + bb) );
//        System.out.println(aa + " - " + bb + " = " + (aa - bb) );
//        System.out.println(aa + " * " + bb + " = " + (aa * bb) );
//        System.out.println(aa + " / " + bb + " = " + ((float)aa / (float)bb) );
        
        
        //논리 부정 연산자
        boolean a = true;
        boolean b = false;
        boolean c = !b;   //b의 값을 반대로 바꾸어 대입한다.
        System.out.println(a);  //true가 출력된다.
        System.out.println(!a); //값을 바꾸어 출력한다.
        
        System.out.println(b);  //false가 출력된다.
        System.out.println(c);  //true가 출력된다.
        
        
    }
 
}
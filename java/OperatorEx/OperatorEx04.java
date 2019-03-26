package OperatorEx;

/*
 * 논리 연산자 ( &&, ||, ^ )
 * 논리연산자는 여러 가지 조건을 동시에 검사할 때 사용하는 연산자로서, 두 항의 값이 Boolean 값일 경우에
 * 사용하는 연산자 입니다.
 * 논리연산자에는 AND(&&)와 OR(||), 그리고 XOR(^) 연산자가 있으며, 
 * AND(&&)는 두항이 모두 참(true)일 경우에만 결과가 참(ture)가 되며
 * OR(||)는 두 항 중 하나라도 참(true)이면 참(true)이 된다. 
 * XOR(^)는 두 항이 서로 다를 경우에는 참(true) 같으면 거짓(false)가 된다.
 */
 
public class OperatorEx04 {
 
    public static void main(String[] args) {
 
        //AND(&&)
        System.out.println( true && true );
        System.out.println( true && false );
        System.out.println( false && true );
        System.out.println( false && false );
        
        //OR(||)
        System.out.println( true || true );
        System.out.println( true || false );
        System.out.println( false || true );
        System.out.println( false || false );
        
        //XOR(^)
        System.out.println( true ^ true );
        System.out.println( true ^ false );
        System.out.println( false ^ true );
        System.out.println( false ^ false );    
        
        int a = 10;
        System.out.println( 5 < a && a < 15 );
        System.out.println(( 5 < a && a < 15) || a % 2 == 0);
        
        a = 4;
        System.out.println( (5 < a && a < 15) && a % 2 == 0 );
        System.out.println( (5 < a && a < 15) || a % 2 == 0 );
        
    }
 
}
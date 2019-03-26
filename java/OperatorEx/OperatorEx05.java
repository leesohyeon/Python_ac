package OperatorEx;
 
/*
 * 비트연산자
 * 비트연산자는 개발자가 직접 비트를 조작할 수 있는 연산자이다.
 * 연산하는 수를 이진수로 표현했을 때 규칙에 따라 알맞는 결과를 반환한다.
 *
 * AND( & )
 * OR( | )
 * XOR( ^ )
 * NOT( ~ )
 */ 
public class OperatorEx05 {
    
    public static void main(String[] args) {
        
        int a = 15;  //1111
        int b = 5;   //0101  
        
        System.out.println( a | b );
        System.out.println( a & b );
        System.out.println( a ^ b );  //1010
        
        System.out.println( a >> 2 );  //1111 --> 11(십진수 : 3)
        System.out.println( b << 4 );  //0101 <-- 01010000(십진수 : 80)
                
        //XOR 연산자를 이용한 암호화 복호화 예제
        int i = 9654;
        int x = i ^ 7890;
        System.out.println(x);
        int r = x ^ 7890;
        System.out.println(r);
        
        //삼항연산자
        int age = 17;
        System.out.println( age > 19 ? "성인입니다." : "청소년입니다." );
        
        String Mess = "성입니다.";
        if( 19 < age )
        {
            Mess = "성입니다.";
        }
        else //if( age <=  19)
        {
            Mess = "청소년입니다.";
        }
        System.out.println(Mess);
        
        //대입연산자
        int aaa =3;
        int bbb = 5;
        
        bbb = 4;
        System.out.println(bbb);
        
        aaa += 1;   // aaa = aaa + 1;
        System.out.println(aaa);
        aaa /= 2;   // aaa = aaa / 2;
        System.out.println(aaa);        
        aaa *= 4;   // aaa = aaa * 4;
        System.out.println(aaa);
        
    }
}
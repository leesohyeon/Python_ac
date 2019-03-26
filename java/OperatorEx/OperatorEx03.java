package OperatorEx;
 
//# 증감 연산자
// ++, --
 
//# 비교 연산자
//비교 연산자는 실제 부등호의 방향이 결과와 일치하면 참(true)을, 다르면 거짓(false)을 반환한다.
 
public class OperatorEx03 {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
 
        int a = 3;
        a = a + 1;
        a++;   //a = a + 1;
        ++a;   //a = a + 1;
        System.out.println(a);
        
        int bb = 10;
        ++bb;
        int result1 = bb;
        System.out.println("변수 result1의 값 : " + result1);
        int cc = 10;
        int result2 = cc;
        System.out.println("변수 result2의 값 : " + result2);
        cc++;
 
        int ee = 10;
        ee--;   //ee = ee - 1;
        --ee;   //ee = ee - 1;
        int ret = ee--;
        System.out.println(ee);
        
        int xx = 10;
        System.out.println(xx--);
        int yy = 10;
        System.out.println(--yy);
        
        for(int ii = 0; ii <10; ii++)
        {
            
        }
        
        //-- 비교 연산자
        int aaa = 10;
        int bbb = 20;
        int ccc = 30;
        System.out.println( aaa < bbb );
        System.out.println( aaa > bbb );
        System.out.println( aaa + bbb <= ccc );
        System.out.println( aaa + bbb >= ccc );
        
        //-- 등가비교 연산자 ==, !=
        //등가비교는 양변이 같은지 다른지 비교하는 연산자
        
        double i = 3.14;
        double j = 5.14;
        System.out.println( i == j );
        System.out.println( i != j );
            
        String c1 = "Hello JAVA";
        System.out.println(c1.equals("Hello JAVA"));
        System.out.println(c1 == "Hello JAVA");
    }
 
}
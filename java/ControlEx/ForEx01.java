package ControlEx;
 
/*
 * for문의 원형 (반복문)
 * for(초기식; 조건식; 증감식)
 * {
 *    //반복문
 * }
 */
public class ForEx01 {
 
    public static void main(String[] args) {
 
//        for(int a = 0; a < 5; a++)   //이 패턴일때 여기서 5는 for문을 도는 횟수
//        {
//            System.out.printlnaa);
//            //a 변수의 변화는 a = 0 ~ 4 까지 출력이 된다.
//        }
//        
//        for(int b = 0; b < 10; b++)  //반복횟수 : 10
//        {
//            System.out.println(b);  //변화값은 0 ~ 9 까지가 된다.
//        }
//        
//        for(int c = 0; c < 100; c++)  //반복횟수 : 100
//        {
//            System.out.println(c);  //변화값은 0 ~ 99 까지가 된다.
//        }
//        
//        
//        for(int d = 1; d < 10; d++)  //반복횟수 : 9
//        {            
//            System.out.println(d);  //변화값은 1 ~ 9 까지가 된다.
//        }
        
//        //문제1 : 구구단의 7단을 for을 이용해서 출력해 보자
//        System.out.println("<구구단 7단>");
//        for(int a = 1; a < 10; a++)
//        {
//            //a = 1 ~ 9
//            System.out.printf("7 * %d = %d\n", a, (7 * a));
//        }
//        
//        System.out.print("\n\n");
        
        //문제2 : 1부터 10까지의 합을 구하는 문제(중간과정도 출력해 주세요.)
        //for문을 이용해서 구해보자~~
        // 0 + 1 = 1
        // 1 + 2 = 3
        // 3 + 3 = 6
        //   :
        //   :
        // ? + 10 = 55
        
//        int Hap = 0;        
//        for(int a = 1; a < 11; a++)
//        {
//            System.out.printf("%d + %d = %d\n", Hap, a, (Hap + a));
//            Hap = Hap + a;
//        }
                
        //이중 for문
        //구구단 2단부터 9단까지 이중 for문을 이용해서 한번에 출력할 수 있다.
        System.out.printf("<구구단>\n\n");
        for(int Dan = 2; Dan < 10; Dan++)  //a_Dan 변수의 변화는 2 ~ 9 까지 변함 
        {
            System.out.printf("---%d단---\n", Dan);
            for(int Add = 1; Add  < 10; Add++) //a_Add 변수의 변화는 1 ~ 9 까지 변함 
            {
                System.out.printf("%d * %d = %d\n", Dan, Add, (Dan * Add));
            }//1부터 9까지 순환하게 됨
            
            System.out.print("\n");
            
        }//2단부터 9단까지 순환하게 됨
        
    }
 
}
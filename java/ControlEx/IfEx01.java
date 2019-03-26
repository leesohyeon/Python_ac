package ControlEx;
 
// if문의 3가지 케이스
 
import java.util.Scanner;
 
public class IfEx01 {
 
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("숫자 하나를 입력해 주세요 : ");
        int i = sc.nextInt();
        
//1번째 케이스  //9를 입력하면 아래 조건에 맞는 두문장을 출력 실행된다.
        if(i == 7)
        {
            System.out.println("7을 입력 하셨습니다.");
        }
        if(i == 8)
        {
            System.out.println("8을 입력 하셨습니다.");
        }
        if(i == 9)
        {
            System.out.println("9을 입력 하셨습니다.");
        
        if(i == 9)
        {
            System.out.println("다시 9를 입력 하셨습니다.");
        }
        
        System.out.print("\n\n");
        
//2번째 케이스  //9를 입력하면 아래 조건에 맞는 한문장만 출력 실행하고 나머지는 건너뜀
        if(i == 7)
        {
            System.out.println("7을 입력 하셨습니다.");
        }
        else if(i == 8)
        {
            System.out.println("8을 입력 하셨습니다.");
        }
        else if(i == 9)
        {
            System.out.println("9를 입력 하셨습니다.");
        }
        else if(i == 9)
        {
            System.out.println("다시 9를 입력 하셨습니다.");
        }
        
        System.out.print("\n\n");
        
//3번째 케이스    //12를 입력하게 되면 else라도 출력 실행된다.
        if(i == 7)
        {
            System.out.println("7을 입력 하셨습니다.");
        }
        else if(i == 8)
        {
            System.out.println("8을 입력 하셨습니다.");
        }
        else if(i == 9)
        {
            System.out.println("9를 입력 하셨습니다.");
        }
        else
        {
            System.out.println("7, 8, 9도 아닙니다.");
        }
        
        
    }
 
}
}
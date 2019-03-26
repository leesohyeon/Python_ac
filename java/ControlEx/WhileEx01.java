package ControlEx;
 
import java.util.Random;
 
import javax.swing.JOptionPane;
 /*
  * while문은  for 의 친척
  *
  * for문은 반복횟수가 제한되어 있을 때 주로 사용한다.
  * while문은 주로 무한루프를 돌릴 때 사용한다.
  */
public class WhileEx01 {
 
    public static void main(String[] args) {
 
//        int a = 0;
//        while(a < 10)
//        {
//            System.out.println(a);
//            a++;
//        }
//        
//        System.out.print("\n\n");
//        
//        for(int i = 0; i < 10; i++)
//        {
//            System.out.println(i);
//        }
        
        int Gold = 1000;
        
        while(true) //무한반복
        {
            Random rd = new Random();
            int rand = rd.nextInt(5) + 1; 
            
            int InUser = Integer.parseInt(JOptionPane.showInputDialog(
                            "지금 나온 주사위 숫자를 예측하여 짝수면 1, 홀수면 2를 입력해 주세요."));
            
            if(InUser == 1 && (rand % 2) == 0)       //짝수인 경우
            {
                Gold = Gold + 100;
                String a_str = "(주사위값 : " + rand + ") 축하합니다. 맞추셨어요. 보상 골드 100"
                        + " 보유골드(" + Gold + ")";
                JOptionPane.showMessageDialog(null, a_str);
            }
            else if(InUser == 2 && (rand % 2) == 1)  //홀수인 경우
            {
                Gold = Gold + 100;
                String a_str = "(주사위값 : " + rand + ") 축하합니다. 맞추셨어요. 보상 골드 100"
                        + " 보유골드(" + Gold + ")";
                JOptionPane.showMessageDialog(null, a_str);
            }
            else
            {
                Gold = Gold - 500;
                String a_str = "(주사위값 : " + rand + ") 틀리셨습니다. 다음에 도전해 주세요."
                        + " 보유골드(" + Gold + ")";
                JOptionPane.showMessageDialog(null, a_str);                
            }
            
            if(Gold <= 0)
            {
                Gold = 0;
                break;         //<--While문 탈출하는 명령어가 된다.
            }
            //while문 안에서 break; 키워드는 while문 탈출 명령어가 된다.
            
        }//while(true)
        
    }
 
}
